
from pydantic import BaseModel

class Product_schema(BaseModel):
    id:int
    partner_company_id:int 
    name:str
    description:str
    price_money:str
    price_points:int
    tags:str


