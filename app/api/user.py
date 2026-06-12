from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserResponse, Token # UserLogin
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.user_service import create_user, login_user
from fastapi.security import OAuth2PasswordRequestForm
from app.api.dependencies import get_current_user # admin_required
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user_data)
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        access_token = login_user(
            db,
            form_data
        )
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# @router.get("/admin", response_model=UserResponse)
# def get_admin(current_user: User = Depends(admin_required)):
#     return current_user



# Handles:

# Request
# Response
# Status Codes
# Authentication

