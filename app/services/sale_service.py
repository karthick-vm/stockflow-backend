from sqlalchemy.orm import Session

from app.schemas.sale import SaleItemCreate
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product

def create_sale(db: Session, user_id: int, items: list[SaleItemCreate]):
    total_amount = 0
    sale = Sale(
        created_by=user_id,
        total_amount=0
    )
    db.add(sale)
    db.flush()
    for item in items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise ValueError(f"Product {item.product_id} not found")
        if product.quantity < item.quantity:
            raise ValueError(f"Insufficient stock for {product.name}")
        subtotal = (product.price * item.quantity)
        total_amount += subtotal
        product.quantity -= item.quantity
        
        sale_item = SaleItem(
            sale_id=sale.id,
            product_id=product.id,
            quantity=item.quantity,
            unit_price=product.price,
            subtotal=subtotal
        )
        db.add(sale_item)

    sale.total_amount = total_amount
    db.commit()
    db.refresh(sale)
    return sale


