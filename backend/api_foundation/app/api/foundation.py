
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import Foundation_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

foundation = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@foundation.get('/')
def read_root():
    return  {'message':'civica punto'}

@foundation.post('/')
def post_foundation(post:Foundation_schemas, db:Session=Depends(get_db)):
    
    foundation = Foundation_model(
        name = post.name,
        address = post.address,
        mail = post.mail,
        budget = post.budget,
        description = post.description,
        user = post.user,
        password = post.password,
    )
    db.add(foundation)
    db.commit()
    db.refresh(foundation)
    return foundation

@foundation.post('/login')
def login(post:Foundation_login, db:Session=Depends(get_db)):
    foundation = db.query(Foundation_model).filter_by(password=post.password, user=post.user).first()
    if(foundation!=None):
        return foundation
    else:
        return {"message": 1216} #No existe