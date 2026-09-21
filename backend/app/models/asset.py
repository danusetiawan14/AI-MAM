from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.models.base import Base
from app.models.base import UUIDMixin
from app.models.base import TimestampMixin


class Asset(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "assets"

    title = Column(String(255))

    description = Column(String)

    file_name = Column(String(500))

    file_path = Column(String(1000))

    media_type = Column(String(50))

    duration = Column(Integer)

    uploaded_by = Column(
        ForeignKey("users.id")
    )