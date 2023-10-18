import ipinfo
import os
from aiocache import SimpleMemoryCache
from aiocache.decorators import cached

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
handler = ipinfo.getHandler(IPINFO_TOKEN)

@cached(ttl=3600, cache=SimpleMemoryCache)  # Cache the result for 1 hour (3600 seconds). Adjust the ttl as needed.
async def get_geolocation(ip_address: str):
    details = handler.getDetails(ip_address)
    return {
        "city": details.city,
        "region": details.region,
        "loc": details.loc  # This contains latitude and longitude
    }
