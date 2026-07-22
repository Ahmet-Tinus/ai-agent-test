from fastapi import FastAPI
from app.database.connection import db
from app.routers.user_router import router as user_router


app = FastAPI()


@app.get("/")
async def root():

    collections = await db.list_collection_names()

    return {
        "database": "Connected",
        "collections": collections
    }

app.include_router(user_router,prefix="/users",tags=["Users"])