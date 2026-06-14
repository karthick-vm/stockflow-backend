from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate
from app.models.product import Product
from app.models.category import Category
from app.models.supplier import Supplier
from app.core.cache import invalidate_reports_cache

def create_product(db: Session, product_data: ProductCreate):
    category = db.query(Category).filter(Category.id == product_data.category_id).first()
    if not category:
        raise ValueError("Category not found")
    supplier = db.query(Supplier).filter(Supplier.id == product_data.supplier_id).first()
    if not supplier:
        raise ValueError("Supplier not found")
    product = Product(**product_data.model_dump())
    db.add(product)
    db.commit()
    invalidate_reports_cache()
    db.refresh(product)
    return product

def get_all_products(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Product).order_by(Product.id).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: int, product_data: ProductCreate):
    product = (db.query(Product).filter(Product.id == product_id).first())
    if not product:
        raise ValueError("Product not found")
    product.name = product_data.name
    product.description = (product_data.description)
    product.price = product_data.price
    product.quantity = (product_data.quantity)
    product.low_stock_threshold = (product_data.low_stock_threshold)
    product.category_id = (product_data.category_id)
    product.supplier_id = (product_data.supplier_id)
    db.commit()
    invalidate_reports_cache()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ValueError("Product not found")
    if product.sale_items:
        raise ValueError("Cannot delete product with sales history")
    db.delete(product)
    db.commit()
    invalidate_reports_cache()

def restock_product(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ValueError("Product not found")
    product.quantity += quantity
    db.commit()
    invalidate_reports_cache()
    db.refresh(product)
    return product

