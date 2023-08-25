import uuid
from decimal import Decimal

from arrow import Arrow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey

from . import ArrowType, AssetEntity, Base, DecimalType, FeeEntity, LabelValueEntity, UserEntity


class TradeEntity(Base):
    __tablename__ = "trade"

    id_: Mapped[uuid.UUID] = mapped_column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    base_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("asset.id"))
    base: Mapped[AssetEntity] = relationship(AssetEntity, foreign_keys=[base_id], lazy="select")

    quote_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("asset.id"))
    quote: Mapped[AssetEntity] = relationship(AssetEntity, foreign_keys=[quote_id], lazy="select")

    fee_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("fee.id"))
    fee: Mapped[FeeEntity] = relationship(FeeEntity, foreign_keys=[fee_id], lazy="select")

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("user.id"))
    user: Mapped[UserEntity] = relationship(UserEntity, foreign_keys=[user_id], lazy="select")

    labels: Mapped[list[LabelValueEntity]] = relationship(LabelValueEntity)

    amount: Mapped[Decimal] = mapped_column(DecimalType())
    price: Mapped[Decimal] = mapped_column(DecimalType())
    placed_at: Mapped[Arrow] = mapped_column(ArrowType())
