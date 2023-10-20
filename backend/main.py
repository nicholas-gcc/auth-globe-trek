from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()  

from routers import auth, user_ips, geolocation  
app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(user_ips.router, prefix="/api/v1", tags=["user-ips"])
app.include_router(geolocation.router, prefix="/api/v1", tags=["geolocation"])
