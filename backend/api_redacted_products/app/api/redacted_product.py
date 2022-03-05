
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import Redacted_product_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

redacted_product = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@redacted_product.get('/')
def read_root():
    return  {'message':'civica punto'}

@redacted_product.post('/')
def post_redacted_product(post:Redacted_product_schema,  db:Session=Depends(get_db)):
    redacted_product = Redacted_product_model(
        product_id = post.product_id,
        student_id = post.student_id,
        amount_poitns = post.amount_points
    )
    db.add(redacted_product)
    db.commit()
    db.refresh(redacted_product)
    return redacted_product
    