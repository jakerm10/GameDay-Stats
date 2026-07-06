from Backend.app.database.session import SessionLocal
from Backend.app.crud.team import create_team


def load_teams(teams):

    db = SessionLocal()

    try:
        for team in teams:
            create_team(db, team)

    finally:
        db.close()