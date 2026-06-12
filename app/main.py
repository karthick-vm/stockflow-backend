from fastapi import FastAPI
from app.api.user import router as user_router
from app.api.category import router as category_router
from app.api.supplier import router as supplier_router
from app.api.product import router as product_router
from app.api.sale import router as sale_router
from app.api.report import router as report_router

app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)
app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(sale_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {"message": "Hello StockFlow"}