from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from Backend.app.database.base import Base


class Stadium(Base):
    __tablename__ = "stadiums"

    id: Mapped[int] = mapped_column(primary_key=True)
    cfbd_id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)

    city: Mapped[str] = mapped_column(String(100), nullable=True)
    state: Mapped[str] = mapped_column(String(30), nullable=True)
    timezone: Mapped[str] = mapped_column(String(100), nullable=True)
    elevation: Mapped[float] = mapped_column(Float, nullable=True)
    
    capacity: Mapped[int] = mapped_column(nullable=True)
    construction_year: Mapped[int] = mapped_column(nullable=True)
    grass: Mapped[bool] = mapped_column(nullable=True)
    dome: Mapped[bool] = mapped_column(nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)