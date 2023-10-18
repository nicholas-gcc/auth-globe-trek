from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from routers import auth, user_ips, geolocation  # Import after loading env variables

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(user_ips.router, prefix="/api/v1", tags=["user-ips"])
app.include_router(geolocation.router, prefix="/api/v1", tags=["geolocation"])  
