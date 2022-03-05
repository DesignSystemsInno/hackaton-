
from pydantic import BaseModel

class Activity_schemas(BaseModel):
    id:int
    id_foundation:int
    name:str
    points:int
    description:str
    tags:str
    location:str
    
    


