import os
import time
import random
import httpx
import asyncio
import gzip
import io
import json

from services import auth_service

AUTH_DOMAIN = os.getenv("AUTH_DOMAIN")
CONNECTION_ID = os.getenv("CONNECTION_ID")


async def fetch_management_api_token():
    token_data = await auth_service.fetch_auth_token()
    return token_data["access_token"]  # Assuming this is the structure of the token response

async def create_export_job():
    token = await fetch_management_api_token()
    headers = {'authorization': f"Bearer {token}", 'content-type': "application/json"}
    
    # Request body
    body = {
        "connection_id": CONNECTION_ID,
        "format": "json",
        "limit": 200,
        "fields": [
            {
                "name": "user_metadata.last_login_ip"
            },
            {
                "name": "user_metadata"
            }
        ]
    }
    
    # Using httpx to make the POST request
    async with httpx.AsyncClient() as client:
        response = await client.post(f"https://{AUTH_DOMAIN}/api/v2/jobs/users-exports", headers=headers, json=body)
        response_data = response.json()
        return response_data["id"]

async def get_job_status(job_id):
    token = await fetch_management_api_token()
    headers = {'authorization': f"Bearer {token}"}
    
    # Using httpx to make the GET request
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://{AUTH_DOMAIN}/api/v2/jobs/{job_id}", headers=headers)
        response_data = response.json()
        return response_data["status"], response_data.get("location")

async def get_file_content(download_link):
    # Using httpx to download the .json.gz file
    async with httpx.AsyncClient() as client:
        response = await client.get(download_link)
        
        # Check if the request was successful
        response.raise_for_status()

        # Decompress the .gz file to get the JSON content
        gzip_content = io.BytesIO(response.content)
        
        user_data = []

        with gzip.GzipFile(fileobj=gzip_content, mode='rb') as f:
            for line in f:
                json_line = json.loads(line.decode('utf-8'))
                ip_address = json_line.get('user_metadata.last_login_ip')
                user_metadata = json_line.get('user_metadata')
                if ip_address and user_metadata:  # ensure the ip_address and user_metadata are not None or empty
                    user_data.append({
                        "ip_address": ip_address,
                        "user_metadata": user_metadata,
                    })

        return user_data



async def fetch_user_ips():
    job_id = await create_export_job()
    
    # Define a maximum timeout period
    timeout = time.time() + 60*5  # 5 minutes
    
    # Initial backoff time and max backoff time
    backoff_time = 0.5  # start with 1 second
    max_backoff = 8  # max 32 seconds

    while True:
        status, download_link = await get_job_status(job_id)
        
        if status == 'completed':
            return await get_file_content(download_link)
        
        elif time.time() > timeout:
            raise Exception("Job did not complete in the specified timeout period")
        
        # Exponential backoff with jitter
        time_to_sleep = backoff_time + random.uniform(0, 0.1 * backoff_time)  # adding 10% jitter
        await asyncio.sleep(time_to_sleep)
        
        # Double the backoff time for next iteration, but do not exceed max_backoff
        backoff_time = min(2 * backoff_time, max_backoff)
