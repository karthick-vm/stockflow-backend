from app.db.base import Base, TimeStampMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime, timezone

class Sale(Base, TimeStampMixin):

    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    total_amount: Mapped[float] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    items = relationship("SaleItem", back_populates="sale")
