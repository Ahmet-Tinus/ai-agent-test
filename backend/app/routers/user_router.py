from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user, list_users


router = APIRouter()

@router.post("/")
async def create_user_endpoint(user: UserCreate):
    return await create_user(user)

@router.get("/")
async def list_users_endpoint():
    return await list_users()