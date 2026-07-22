from datetime import datetime, UTC
from app.database.connection import db
from app.schemas.user_schema import UserCreate
from app.utils.serializer import serialize_user


async def create_user(user: UserCreate):
    users_collection = db["users"]
    user_data = user.model_dump()

    now = datetime.now(UTC)

    user_data["created_at"] = now
    user_data["updated_at"] = now

    result = await users_collection.insert_one(user_data)

    created_user = await users_collection.find_one({"_id": result.inserted_id})

    return serialize_user(created_user)

async def list_users():
    users_collection = db["users"]
    users_cursor = users_collection.find()
    users = await users_cursor.to_list(length=None)
    return [serialize_user(user) for user in users]