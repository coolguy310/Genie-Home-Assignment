import uuid
from decimal import Decimal

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey

from . import AssetEntity, Base, DecimalType


class FeeEntity(Base):
    __tablename__ = "fee"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    currency_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("asset.id"))
    currency: Mapped[AssetEntity] = relationship(AssetEntity, foreign_keys=[currency_id], lazy="select")

    amount: Mapped[Decimal] = mapped_column(DecimalType())
