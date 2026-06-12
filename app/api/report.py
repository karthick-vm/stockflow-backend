from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.api.dependencies import require_manager
from app.models.user import User
from app.schemas.product import ProductResponse
from app.schemas.report import TopSellingProduct, MonthlySalesSummary
from app.services.report_service import get_low_stock_products
from app.services.report_service import get_top_selling_products
from app.services.report_service import monthly_sales_summary

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/low-stock", response_model=list[ProductResponse])
def low_stock_products(db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    return get_low_stock_products(db)

@router.get("/top-selling", response_model=list[TopSellingProduct])
def top_selling_products(db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    return get_top_selling_products(db)

@router.get("/monthly-sales", response_model=list[MonthlySalesSummary])
def monthly_sales_report(db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    return monthly_sales_summary(db)


