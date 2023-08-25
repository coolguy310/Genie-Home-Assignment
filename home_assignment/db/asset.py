import uuid

from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class AssetEntity(Base):
    __tablename__ = "asset"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(VARCHAR(8), nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(16), nullable=False)  # noqa: WPS432
