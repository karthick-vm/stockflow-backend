from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int
    low_stock_threshold: int
    category_id: int
    supplier_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    quantity: int
    low_stock_threshold: int
    category_id: int
    supplier_id: int
    model_config = {"from_attributes": True}

class ReStockProduct(BaseModel):
    quantity: int = Field(gt=0)


