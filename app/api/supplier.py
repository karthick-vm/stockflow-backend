from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.api.dependencies import get_current_user, require_admin

from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.services.supplier_service import (create_supplier as create_supplier_service)
from app.services.supplier_service import (get_all_suppliers as get_all_suppliers_service)
from app.services.supplier_service import (update_supplier as update_supplier_service)
from app.services.supplier_service import (delete_supplier as delete_supplier_service)

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierResponse)
def create_supplier(
supplier_data: SupplierCreate, 
db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        return create_supplier_service(db, supplier_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[SupplierResponse])
def get_all_suppliers(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_suppliers_service(db)

@router.put("/{supplier_id}", response_model=SupplierResponse)
def update_supplier(supplier_id: int, supplier_data: SupplierCreate,
                    db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        return update_supplier_service(db, supplier_id, supplier_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, 
                    db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    try:
        delete_supplier_service(db, supplier_id)
        return {"message": "Supplier deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


