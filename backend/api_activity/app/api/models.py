
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

class Activity_model(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True, index=True)
    id_foundation = Column(Integer)
    name = Column(String(255))
    points = Column(Integer)
    descrioption = Column(String(255))
    tags = Column(String(255))
    location = Column(String(255))


