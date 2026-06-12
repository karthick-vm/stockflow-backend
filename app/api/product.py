from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.api.dependencies import get_current_user, require_manager
from app.schemas.product import ProductCreate, ProductResponse, ReStockProduct
from app.models.user import User
from app.services.product_service import (create_product as create_product_service)
from app.services.product_service import (get_all_products as get_all_products_service)
from app.services.product_service import (update_product as update_product_service)
from app.services.product_service import (delete_product as delete_product_service)
from app.services.product_service import (restock_product as restock_product_service)

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(
product_data: ProductCreate, 
db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    try:
        return create_product_service(db, product_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[ProductResponse])
def get_all_products(skip: int = 0, limit: int = 20, 
                     db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_products_service(db, skip, limit)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductCreate, 
                   db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    try:
        return update_product_service(db, product_id, product_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{product_id}")
def delete_product(product_id: int, 
                   db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    try:
        delete_product_service(db, product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{product_id}/restock", response_model=ProductResponse)
def restock_product(product_id: int, restock_data: ReStockProduct,
                    db: Session = Depends(get_db), current_user: User = Depends(require_manager)):
    try:
        return restock_product_service(db, product_id, restock_data.quantity)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

