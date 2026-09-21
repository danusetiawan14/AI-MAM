from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return {
        "message": "Register endpoint",
        "username": user.username
    }


@router.post("/login")
def login():
    return {
        "message": "Login endpoint"
    }