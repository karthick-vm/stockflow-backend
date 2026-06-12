from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.sale import SaleCreate, SaleResponse
from app.services.sale_service import create_sale as create_sale_service

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleResponse)
def create_sale(
sale_data: SaleCreate, 
db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return create_sale_service(db, current_user.id, sale_data.items)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

