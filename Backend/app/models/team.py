from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from Backend.app.database.base import Base

## makes this entity a database table
class Team(Base): 
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    school: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    abbreviation: Mapped[str] = mapped_column (String(10),nullable=True)
    mascot: Mapped[str] = mapped_column (String(50), nullable=True)

    conference: Mapped[str] = mapped_column (String(100), nullable=True)
    division: Mapped[str] = mapped_column (String(100), nullable=True)
    classification: Mapped[str] = mapped_column (String(10), nullable=True)

    color: Mapped[str] = mapped_column (String(10), nullable=True)
    alternate_color: Mapped[str] = mapped_column (String(10), nullable=True)
    logo_url: Mapped[str] = mapped_column (String(255), nullable=True)
    
    ##stadium_id: Mapped[int] = mapped_column(foreign_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)
