
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

class Foundation_model(Base):
    __tablename__ = 'foundation'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    address = Column(String(255))
    mail = Column(String(255))
    budget = Column(String(255))
    description = Column(String(255))
    user =Column(String(255))
    password = Column(String(255))


