from pydantic import BaseModel, EmailStr

class SupplierCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str | None = None

class SupplierResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str | None
    model_config = {"from_attributes": True}


