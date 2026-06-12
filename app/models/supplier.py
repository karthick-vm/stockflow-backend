from app.db.base import Base, TimeStampMixin

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Supplier(Base, TimeStampMixin):
    
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[str] = mapped_column(String(20))
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)

    products = relationship("Product", back_populates="supplier")
