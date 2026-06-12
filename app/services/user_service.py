from sqlalchemy.orm import Session
from app.schemas.user import UserCreate # UserLogin
from app.models.user import User
from app.core.security import hash_password
# from sqlalchemy import select
from app.core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

def create_user(db: Session, user_data: UserCreate) -> User:
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    # existing_user = db.scalar(select(User).where(User.email == user_data.email))
    if existing_user:
        raise ValueError("Email already exists")
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, form_data: OAuth2PasswordRequestForm):
    db_user = db.query(User).filter(User.name == form_data.username).first()
    # db_user = db.scalar(select(User).where(User.email == form_data.email))
    if not db_user:
        raise ValueError("Invalid credentials")
    if not verify_password(form_data.password, db_user.hashed_password):
        raise ValueError("Invalid credentials")
    access_token = create_access_token(
        {"sub":str(db_user.id)}
    )
    return access_token





# Handles:

# Business Logic
# Database Operations
# Validation Rules