# StockFlow

Inventory Management & Sales Tracking Backend built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

## Features

* JWT Authentication
* Category CRUD
* Supplier CRUD
* Product CRUD
* Product Restocking
* Sales Processing
* Inventory Tracking
* Low Stock Reports
* Top Selling Products Report
* Monthly Sales Summary
* Pagination

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT Authentication

## Project Structure

```text
app/
├── api/
├── models/
├── schemas/
├── services/
├── db/
├── core/

alembic/
```

## Setup

```bash
git clone <repository-url>
cd stockflow

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
```

## API Documentation

```text
http://127.0.0.1:8000/docs
```

## Main Endpoints

```http
POST   /users/register
POST   /users/login

GET    /categories
POST   /categories
PUT    /categories/{id}
DELETE /categories/{id}

GET    /suppliers
POST   /suppliers
PUT    /suppliers/{id}
DELETE /suppliers/{id}

GET    /products
POST   /products
PUT    /products/{id}
DELETE /products/{id}
PATCH  /products/{id}/restock

POST   /sales

GET    /reports/low-stock
GET    /reports/top-selling
GET    /reports/monthly-sales
```

## Concepts Demonstrated

* REST API Design
* JWT Authentication
* Service Layer Architecture
* Database Relationships
* Inventory Management
* Pagination
* Reporting Queries
* Alembic Migrations

```
```
