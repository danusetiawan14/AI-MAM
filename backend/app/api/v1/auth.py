from fastapi import APIRouter

from app.schemas.user import UserCreate
from app.schemas.auth import LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate):

    return {
        "username": user.username,
        "email": user.email,
        "message": "User registered"
    }


@router.post("/login")
def login(data: LoginRequest):

    return {
        "username": data.username,
        "message": "Login request received"
    }