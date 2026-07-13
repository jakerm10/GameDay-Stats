from sqlalchemy.orm import Session

from Backend.app.models.stadium import Stadium


def create_stadium(db: Session, stadium_data):

    stadium = Stadium(**stadium_data)

    db.add(stadium)
    db.commit()
    db.refresh(stadium)

    return stadium