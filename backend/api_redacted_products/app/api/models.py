
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

class Redacted_product_model(Base):
    __tablename__ = 'redacted_product'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    student_id = Column(Integer)
    amount_points = Column(Integer)

