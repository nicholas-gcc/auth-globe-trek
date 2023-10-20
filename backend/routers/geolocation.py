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
        print(f"Time taken to complete export job: {ip_fetch_end - ip_fetch_start} seconds")

        geo_start = time.time()

        # Fetch all geolocations using batch and concurrent processing method
        updated_user_data = await ipinfo_service.fetch_all_geolocations(ip_data)  # Note the change here

        if format == "city":
            geolocations = {}
            for data in updated_user_data:
                if data['geolocation']['latitude'] is None or data['geolocation']['longitude'] is None:
                    continue
                geo = data['geolocation']
                key = f"{geo['city']}, {geo['region']}"
                geolocations[key] = geolocations.get(key, 0) + 1
            output = {"geolocations": geolocations}

        elif format == "coords":
            coordinates = []
            for data in updated_user_data:
                if data['geolocation']['latitude'] is None or data['geolocation']['longitude'] is None:
                    continue
                geo = data['geolocation']
                user_metadata = data['user_metadata']
                loc = geo['loc'].split(',')
                coordinates.append([loc[0], loc[1], user_metadata])
            output = {"coordinates": coordinates}

        else:
            raise HTTPException(status_code=400, detail="Invalid format specified")

        geo_end = time.time()
        print(f"Time taken to geolocate: {geo_end - geo_start} seconds")

        return output

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))