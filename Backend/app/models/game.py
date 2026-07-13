from sqlalchemy import Boolean, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from Backend.app.database.base import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    cfbd_id: Mapped[int] = mapped_column(unique=True)

    start_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=True)
    season: Mapped[int] = mapped_column()
    week: Mapped[int] = mapped_column()
    season_type: Mapped[String] = mapped_column(String(20), nullable=False)
    conference_game: Mapped[bool] = mapped_column(nullable=True)
    
    stadium_id: Mapped[Optional[int]] = mapped_column(ForeignKey("stadiums.id"), nullable=True)
    neutral_site: Mapped[bool] = mapped_column(nullable=True)

    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    home_team_points: Mapped[int] = mapped_column(nullable=True)
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    away_team_points: Mapped[int] = mapped_column(nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)