import uuid

from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey

from . import Base


class LabelKeyEntity(Base):
    __tablename__ = "label_key"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column("name", VARCHAR(), nullable=False, unique=True)


class LabelValueEntity(Base):
    __tablename__ = "label_value"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    key_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("label_key.id"), nullable=False)
    key: Mapped[LabelKeyEntity] = relationship(LabelKeyEntity, foreign_keys=[key_id], lazy="select")

    value: Mapped[str] = mapped_column("value", VARCHAR(), nullable=True)

    trade_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("trade.id"), nullable=False)
