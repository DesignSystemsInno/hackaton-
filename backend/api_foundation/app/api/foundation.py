
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import foundation_model
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

@floors.get('/')
def read_root():
    return  {'message':'www.panda.com'}

