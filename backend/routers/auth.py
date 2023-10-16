from fastapi import APIRouter, HTTPException
from services import auth_service

router = APIRouter()

@router.post("/auth/token/")
async def create_auth_token():
    try:
        token_data = await auth_service.fetch_auth_token()
        return token_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
