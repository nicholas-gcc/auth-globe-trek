from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from routers import auth  # Import after loading env variables

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
