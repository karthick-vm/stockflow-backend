from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.product import Product
from app.models.sale_item import SaleItem
from app.models.sale import Sale

def get_low_stock_products(db: Session):
    products = db.query(Product).all()
    return [
        product for product in products if product.quantity <= product.low_stock_threshold
    ]

def get_top_selling_products(db: Session):
    results = (
        db.query(Product.name, func.sum(SaleItem.quantity).label("total_sold"))
        .join(SaleItem, Product.id == SaleItem.product_id)
        .group_by(Product.id, Product.name)
        .order_by(func.sum(SaleItem.quantity).desc())
        .all()
    )
    return [
        {"product_name": product_name, "total_sold": total_sold} 
        for product_name, total_sold in results
    ]

def monthly_sales_summary(db: Session):
    results = (
        db.query(func.date_trunc("month", Sale.created_at).label("month"),
                 func.sum(Sale.total_amount).label("revenue"))
        .group_by("month")
        .order_by("month")
        .all()
    )
    return [
        {"month": month, "revenue": revenue}
        for month, revenue in results
    ]

