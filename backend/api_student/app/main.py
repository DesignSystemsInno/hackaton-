
from fastapi import FastAPI
from app.api.student import student
from fastapi.middleware.cors import CORSMiddleware
import os 

app = FastAPI(openapi_url='/api/v1/student/openapi.json', docs_url='/api/v1/student/docs')

LOCAL_HOST_PORT = os.getenv('LOCAL_HOST_PORT')
IP_HOST_PORT = os.getenv('IP_HOST_PORT') 
origins = ["*"]
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

app.include_router(student, prefix='/api/v1/student', tags=['student'])


