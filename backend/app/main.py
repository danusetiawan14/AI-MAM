from fastapi import FastAPI

from app.db.database import engine

from app.models.base import Base
from app.models.role import Role
from app.models.user import User
from app.models.asset import Asset

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.assets import router as assets_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-MAM API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(assets_router)


@app.get("/")
def root():
    return {
        "message": "AI-MAM API Running"
    }