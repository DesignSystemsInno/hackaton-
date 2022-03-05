
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import Activity_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

activity = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@activity.get('/')
def read_root():
    return  {'message':'civica punto'}

@activity.post('/')
def post_activity(post:Activity_schemas,  db:Session=Depends(get_db)):
    activity = Activity_model(
        id_foundation = post.id_foundation,
        name = post.name,
        points = post.points,
        description = post.description,
        tags = post.tags,
        location = post.location
    )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@activity.get('/activity')
def get_all_activity(db:Session=Depends(get_db)):
    activities = db.query(Activity_model).all()
    return activities



