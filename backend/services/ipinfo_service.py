import ipinfo
import os
import asyncio
from aiocache import SimpleMemoryCache
from aiocache.decorators import cached

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
handler = ipinfo.getHandler(IPINFO_TOKEN)

# Asynchronously get details of a batch of IP addresses
@cached(ttl=3600, cache=SimpleMemoryCache)  # Cache the result for 1 hour.
async def get_geolocations_batch(ip_addresses: list):
    # This is not truly async, but the caching makes it worth including in an async function
    details = handler.getBatchDetails(ip_addresses)
    return details

# Function to split a list into smaller batches
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Asynchronously fetch geolocation details for all IP addresses using batching and parallel processing
async def fetch_all_geolocations(ip_addresses):
    # Split IP addresses into batches of 10 (adjust as needed)
    ip_batches = list(chunks(ip_addresses, 10))
    
    # Use asyncio to fetch geolocations for all batches concurrently
    all_geolocations = await asyncio.gather(*[get_geolocations_batch(batch) for batch in ip_batches])
    
    # Flatten the list of dictionaries into one dictionary
    merged_geolocations = {}
    for batch_result in all_geolocations:
        merged_geolocations.update(batch_result)
    
    return merged_geolocations

