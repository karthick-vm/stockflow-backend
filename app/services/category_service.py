from sqlalchemy.orm import Session

from app.schemas.category import CategoryCreate
from app.models.category import Category

def create_category(db: Session, category_data: CategoryCreate):
    existing_category = db.query(Category).filter(Category.name == category_data.name).first()
    if existing_category:
        raise ValueError("Category Already Exists")
    category = Category(**category_data.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_all_categories(db: Session):
    return db.query(Category).all()

def update_category(db: Session, category_id: int, category_data: CategoryCreate):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise ValueError("Category not found")
    category.name = category_data.name
    category.description = category_data.description
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise ValueError("Category not found")
    if category.products:
        raise ValueError("Cannot delete category with products")
    db.delete(category)
    db.commit()


