from fastapi import APIRouter, HTTPException
from services import user_ips_service, ipinfo_service
import time
from typing import Optional

router = APIRouter()

@router.get("/geolocation/user-ips/")
async def get_user_ips_data(format: Optional[str] = "city"):
    start_time = time.time()

    try:
        ip_fetch_start = time.time()
        ip_data = await user_ips_service.fetch_user_ips()
        ip_fetch_end = time.time()
        print(f"Time taken to fetch IPs: {ip_fetch_end - ip_fetch_start} seconds")
        
        ip_addresses = ip_data["ip_addresses"]

        geo_start = time.time()
        
        # Fetch all geolocations using batch and concurrent processing method
        all_geolocations = await ipinfo_service.fetch_all_geolocations(ip_addresses)

        if format == "city":
            geolocations = {}
            for ip, geo in all_geolocations.items():
                key = f"{geo['city']}, {geo['region']}"
                geolocations[key] = geolocations.get(key, 0) + 1
            output = {"geolocations": geolocations}

        elif format == "coords":
            coordinates = []
            for ip, geo in all_geolocations.items():
                loc = geo['loc'].split(',')
                coordinates.append(tuple(loc))
            coordinates_list = list(map(list, coordinates))
            output = {"coordinates": coordinates_list}

        else:
            raise HTTPException(status_code=400, detail="Invalid format specified")

        geo_end = time.time()
        print(f"Total time taken for get_user_ips_data: {geo_end - geo_start} seconds")
        
        return output

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
