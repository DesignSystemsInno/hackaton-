
from pydantic import BaseModel

class Foundation_schemas(BaseModel):
    id:int
    name:str
    address:str
    mail:str
    budget:str
    description:str
    user:str
    password:str

class Foundation_login(BaseModel):
    user:str
    password:str