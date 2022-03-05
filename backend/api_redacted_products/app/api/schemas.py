
from pydantic import BaseModel

class Redacted_product_schema(BaseModel):
    id:int
    product_id:int
    student_id:int
    amount_points:int



