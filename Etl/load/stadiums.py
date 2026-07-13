from Backend.app.database.session import SessionLocal
from Backend.app.crud.stadium import create_stadium


def load_stadiums(stadiums):

    db = SessionLocal()

    try:
        for stadium in stadiums:
            create_stadium(db, stadium)

    finally:
        db.close()