from Backend.app.database.base import Base
from Backend.app.database.connection import engine
import app.models 

Base.metadata.create_all(bind=engine)