from fastapi import APIRouter

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.user import UserCreate

from fastapi import HTTPException

from app.models.user import User

from app.core.security import hash_password

from app.services.user_service import (
    get_user_by_username,
    get_user_by_email
)

from app.schemas.auth import TokenResponse

from app.services.auth_service import (
    authenticate_user
)

from app.core.security import (
    create_access_token
)

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_username(
        db,
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = get_user_by_email(
        db,
        user.email
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "id": str(new_user.id),
        "username": new_user.username,
        "email": new_user.email
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "username": user.username
        }
    )

    return TokenResponse(
        access_token=access_token
    )