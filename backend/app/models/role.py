from sqlalchemy import Column
from sqlalchemy import String

from app.models.base import Base
from app.models.base import UUIDMixin
from app.models.base import TimestampMixin


class Role(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "roles"

    name = Column(
        String(50),
        unique=True,
        nullable=False
    )

    description = Column(
        String(255)
    )