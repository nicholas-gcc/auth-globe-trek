from fastapi import APIRouter, HTTPException
from services import user_ips_service, ipinfo_service
import time

router = APIRouter()

@router.get("/geolocation/user-ips/")
async def get_user_ips_geolocation():
    start_time = time.time()

    try:
        ip_fetch_start = time.time()
        ip_data = await user_ips_service.fetch_user_ips()
        ip_fetch_end = time.time()
        print(f"Time taken to fetch IPs: {ip_fetch_end - ip_fetch_start} seconds")
        
        ip_addresses = ip_data["ip_addresses"]

        geolocations = {}
        geo_start = time.time()
        for ip in ip_addresses:
            geo = await ipinfo_service.get_geolocation(ip)
            
            key = f"{geo['city']}, {geo['region']}"
            geolocations[key] = geolocations.get(key, 0) + 1
        
        end_time = time.time()
        print(f"Total time taken for get_user_ips_geolocation: {end_time - geo_start} seconds")
        
        return {"geolocations": geolocations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

