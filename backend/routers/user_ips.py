from fastapi import APIRouter, HTTPException
from services import user_ips_service

router = APIRouter()

@router.get("/user-ips/")
async def get_user_ips():
    try:
        return await user_ips_service.fetch_user_ips()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
