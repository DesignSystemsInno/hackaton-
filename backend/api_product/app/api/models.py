
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

class Product_model(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    partner_company_id  = Column(Integer)
    name = Column(String(255))
    description = Column(String(255))
    price_money = Column(String(255))
    price_points = Column(Integer)
    tags = Column(String(255))

