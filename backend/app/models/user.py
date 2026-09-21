from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.base import UUIDMixin
from app.models.base import TimestampMixin


class User(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "users"

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    role_id = Column(
        ForeignKey("roles.id")
    )

    role = relationship("Role")