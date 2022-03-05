mkdir app
mkdir app/api
cp ../api_clientes/Dockerfile .
cp ../api_clientes/requirements.txt .
cp ../api_clientes/app/api/conexion_db.py app/api/db_connection.py
echo "ingrese el nombre de la api"
read api_name
echo "
from fastapi import FastAPI
from app.api.${api_name} import ${api_name}
from fastapi.middleware.cors import CORSMiddleware
import os 

app = FastAPI(openapi_url='/api/v1/${api_name}/openapi.json', docs_url='/api/v1/${api_name}/docs')

LOCAL_HOST_PORT = os.getenv('LOCAL_HOST_PORT¿)
IP_HOST_PORT = os.getenv('IP_HOST_PORT') 
origins = [
 LOCAL_HOST_PORT,
 IP_HOST_PORT
 
]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=['*'],
 allow_headers=['*'],
)

@app.on_event('startup')
async def startup():
    print('startup')

@app.on_event('shutdown')
async def shutdown():
    print('shutdown')

app.include_router(${api_name}, prefix='/api/v1/${api_name}', tags=['${api_name}'])

">> app/main.py
echo "
from unicodedata import name
from fastapi import APIRouter
from app.api.db_connection import Base, SessionLocal, Engine
from app.api.schemas import *
from app.api.models import ${api_name}_model
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
#from fastapi.response import RedirectResponse
Base.metadata.create_all(bind=Engine)

${api_name} = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@floors.get('/')
def read_root():
    return  {'message':'www.panda.com'}
" >> app/api/${api_name}.py
echo "
from pydantic import BaseModel

class ${api_name}_schemas(BaseModel):
    id:int

" >> app/api/schemas.py
echo "
from sqlalchemy import Column, Integer, String
from app.api.db_connection import Base

Class ${api_name}_model(Base):
    __tablename__ = '${api_name}
    id = Column(Integer, primary_key=True, index=True)
" >> app/api/models.py
Y | conda create --name cerex-api_${api_name} python=3 
conda activate "panda-api_${api_name}"
pip install -r requirements.txt 
echo "fin"
