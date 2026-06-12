from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.api.dependencies import get_current_user, require_admin

from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import (create_category as create_category_service)
from app.services.category_service import (get_all_categories as get_all_categories_service)
from app.services.category_service import (update_category as update_category_service)
from app.services.category_service import (delete_category as delete_category_service)

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(
category_data: CategoryCreate, 
db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        return create_category_service(db, category_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_categories_service(db)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category_data: CategoryCreate,
                    db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        return update_category_service(db, category_id, category_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{category_id}")
def delete_category(category_id: int, 
                    db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        delete_category_service(db, category_id)
        return {"message": "Category deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


