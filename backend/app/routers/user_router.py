from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user
router = APIRouter()
@router.post("/")
async def create_user_endpoint(user: UserCreate):
    return await create_user(user)