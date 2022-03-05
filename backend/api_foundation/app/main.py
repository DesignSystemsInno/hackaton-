
from fastapi import FastAPI
from app.api.foundation import foundation
from fastapi.middleware.cors import CORSMiddleware
import os 

app = FastAPI(openapi_url='/api/v1/foundation/openapi.json', docs_url='/api/v1/foundation/docs')

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

app.include_router(foundation, prefix='/api/v1/foundation', tags=['foundation'])


