from sqlalchemy.orm import Session
from sqlalchemy import func
import json

from app.core.redis import redis_client
from app.models.product import Product
from app.models.sale_item import SaleItem
from app.models.sale import Sale
from app.schemas.product import ProductResponse

def get_low_stock_products(db: Session):
    cache_key = "report:low_stock"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("LOW STOCK CACHE HIT")
        return json.loads(cached_data)
    print("LOW STOCK CACHE MISS")
    low_stock_products = db.query(Product).filter(Product.quantity <= Product.low_stock_threshold).all()
    response_data = [ProductResponse.model_validate(product).model_dump() 
                     for product in low_stock_products]
    redis_client.set(cache_key, json.dumps(response_data), ex=300)
    return response_data


def get_top_selling_products(db: Session):
    cache_key = "report:top_selling"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("TOP SELLING CACHE HIT")
        return json.loads(cached_data)
    print("TOP SELLING CACHE MISS")
    results = (
        db.query(Product.name, func.sum(SaleItem.quantity).label("total_sold"))
        .join(SaleItem, Product.id == SaleItem.product_id)
        .group_by(Product.id, Product.name)
        .order_by(func.sum(SaleItem.quantity).desc())
        .all()
    )
    response_data = [
        {"product_name": product_name, "total_sold": total_sold} 
        for product_name, total_sold in results
    ]
    redis_client.set(cache_key, json.dumps(response_data), ex=300)
    return response_data


def monthly_sales_summary(db: Session):
    cache_key = "report:monthly_sales"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("MONTHLY SALES CACHE HIT")
        return json.loads(cached_data)
    print("MONTHLY SALES CACHE MISS")
    results = (
        db.query(func.date_trunc("month", Sale.created_at).label("month"),
                 func.sum(Sale.total_amount).label("revenue"))
        .group_by("month")
        .order_by("month")
        .all()
    )
    response_data = [
        {"month": month.strftime("%Y-%m"), "revenue": float(revenue)}
        for month, revenue in results
    ]
    redis_client.set(cache_key, json.dumps(response_data), ex=300)
    return response_data

