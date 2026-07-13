from Backend.app.database.base import Base
from Backend.app.database.connection import engine

from Backend.app.models import Team, Stadium

Base.metadata.create_all(bind=engine)