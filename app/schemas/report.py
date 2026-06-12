from pydantic import BaseModel
from datetime import datetime

class TopSellingProduct(BaseModel):
    product_name: str
    total_sold: int

class MonthlySalesSummary(BaseModel):
    month: datetime
    revenue: float

