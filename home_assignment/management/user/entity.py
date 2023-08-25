from sqlalchemy import VARCHAR, Integer
from sqlalchemy.sql.schema import Column

from ...db.base import Base  # type: ignore[misc]


class UserEntity(Base):
    __tablename__ = "user"

    id_ = Column("id", Integer(), primary_key=True, autoincrement=True)
    username = Column("username", VARCHAR(), nullable=False, unique=True)
