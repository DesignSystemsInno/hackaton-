
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import Student_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

student = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@student.get('/')
def read_root():
    return  {'message':'civica punto'}


@student.post('/')
def post_student(post:Student_schemas, db:Session=Depends(get_db)):
    student = Student_model(
        name = post.name,
        last_name = post.last_name,
        identification_document = post.identification_document,
        available_points = post.available_points,
        history_points = post.history_points,
        user = post.user,
        password = post.password,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@student.post('/login')
def login(post:Student_login, db:Session=Depends(get_db)):
    student = db.query(Student_model).filter_by(user=post.user, password=post.password).first()
    if(student!=None):
        return student
    else:
        return {"message": 1216}

@student.put('/available_points/{student_identification_document}')
def post_available_points(student_identification_document:int, post:Student_available_points, db:Session=Depends(get_db)):
    student = db.query(Student_model).filter_by(identification_document=student_identification_document).first()

    if(student!=None):
        student.available_points = post.available_points + student.available_points
        db.commit()
        db.refresh(student)
        return student
    else:
        return {"message": 1216}

@student.put('/deduct_points/{student_identification_document}')
def post_deduc_points(student_identification_document:int, post:Student_available_points, db:Session=Depends(get_db)):
    student = db.query(Student_model).filter_by(identification_document=student_identification_document).first()

    if(student!=None):
        student.available_points = student.available_points - post.available_points 
        db.commit()
        db.refresh(student)
        return student
    else:
        return {"message": 1216}

