from sqlalchemy.orm import Session

from app.schemas.supplier import SupplierCreate
from app.models.supplier import Supplier

def create_supplier(db: Session, supplier_data: SupplierCreate):
    existing_supplier = db.query(Supplier).filter(Supplier.name == supplier_data.name).first()
    if existing_supplier:
        raise ValueError("Supplier Already Exists")
    supplier = Supplier(**supplier_data.model_dump())
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

def get_all_suppliers(db: Session):
    return db.query(Supplier).all()

def update_supplier(db: Session, supplier_id: int, supplier_data: SupplierCreate):
    supplier = (db.query(Supplier).filter(Supplier.id == supplier_id).first())
    if not supplier:
        raise ValueError("Supplier not found")
    supplier.name = supplier_data.name
    supplier.email = supplier_data.email
    supplier.phone = supplier_data.phone
    supplier.address = supplier_data.address
    db.commit()
    db.refresh(supplier)
    return supplier

def delete_supplier(db: Session, supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise ValueError("Supplier not found")
    if supplier.products:
        raise ValueError("Cannot delete supplier with products")
    db.delete(supplier)
    db.commit()


