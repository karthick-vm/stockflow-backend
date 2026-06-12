from pydantic import BaseModel, EmailStr

from app.models.user import UserRole

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    model_config = {"from_attributes": True}

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

class Token(BaseModel):
    access_token: str
    token_type: str
