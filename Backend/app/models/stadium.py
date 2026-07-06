from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from Backend.app.database.base import Base


class Stadium(Base):
    __tablename__ = "stadiums"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(30), nullable=False)
    timezone: Mapped[str] = mapped_column(String(100), nullable=False)
    elevation: Mapped[int] = mapped_column(nullable=False)
    
    capacity: Mapped[int] = mapped_column(String(100), nullable=True)
    construction_year: Mapped[int] = mapped_column(nullable=True)
    grass: Mapped[bool] = mapped_column(nullable=True)
    dome: Mapped[bool] = mapped_column(nullable=True)