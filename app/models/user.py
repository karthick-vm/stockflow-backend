from app.db.base import Base, TimeStampMixin

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    SALES = "sales"

class User(Base, TimeStampMixin):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(String(50), default=UserRole.SALES)


