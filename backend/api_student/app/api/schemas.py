
from pydantic import BaseModel

class Student_schemas(BaseModel):
    id:int
    name:str
    last_name:str
    identification_document:str
    available_points:int
    history_points:int
    user:str
    password:str

class Student_login(BaseModel):
    user:str
    password:str

class Student_available_points(BaseModel):
    available_points:int
    
