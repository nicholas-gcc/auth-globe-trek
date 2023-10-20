import httpx
import os

AUTH_DOMAIN = os.getenv("AUTH_DOMAIN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUDIENCE = os.getenv("AUDIENCE")


async def fetch_auth_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://{AUTH_DOMAIN}/oauth/token",
            json={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "audience": AUDIENCE,
                "grant_type": "client_credentials"
            }
        )
        response.raise_for_status()  # Will raise an exception for 4xx/5xx responses
        return response.json()
