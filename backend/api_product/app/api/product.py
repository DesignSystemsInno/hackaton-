
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import Product_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

product = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@product.get('/')
def read_root(db:Session=Depends(get_db)):
    products = db.query(Product_model).all()
    return products

@product.post('/')
def post_product(post:Product_schema, db:Session=Depends(get_db)):
    product = Product_model(
        name = post.name,
        partner_company_id = post.partner_company_id,
        description = post.description,
        price_money = post.price_money,
        price_points = post.price_points,
        tags = post.tags
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product



