import uuid

from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserEntity(Base):
    __tablename__ = "user"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username: Mapped[str] = mapped_column("username", VARCHAR(), nullable=False, unique=True)
