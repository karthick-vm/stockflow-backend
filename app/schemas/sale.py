from pydantic import BaseModel

class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int

class SaleCreate(BaseModel):
    items: list[SaleItemCreate]

class SaleResponse(BaseModel):
    id: int
    total_amount: float
    model_config = {"from_attributes": True}

