
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

class Student_model(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    last_name = Column(String(255))
    identification_document = Column(String(255))
    available_points = Column(Integer)
    history_points = Column(Integer)
    user = Column(String(255))
    password = Column(String(255))
