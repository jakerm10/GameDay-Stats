from sqlalchemy.orm import Session
from Backend.app.models.team import Team


def create_team(db: Session, team_data: dict):

    team = Team(**team_data)

    db.add(team)
    db.commit()
    db.refresh(team)

    return team