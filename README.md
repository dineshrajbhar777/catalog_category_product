# Categories and Products (Catalog)

# Technology used
  - Python 3.8.3
  - Django 3.1.2
  - Postgres 9.5.22

# Backend
  - Django==3.1.2
  - django-filter==2.4.0
  - django-rest-swagger==2.2.0
  - djangorestframework==3.12.1
  - psycopg2==2.8.6

# Backend steps to follow
  1. pip install -r requirements.txt
  2. python manage.py makemigrations
  3. python manage.py migrate
  4. python manage.py createsuperuser
  5. python manage.py runserver

# Expected output:
  - Add a category. (/category)
  - Add Product mapped to a category or categories. (/product)
  - Get all categories with all its child categories mapped to it. (/category)
  - Get all products by a category. (/category/{category_id}/product)
  - Get all categories by a product. (/product/{product_id}/category)
  - Update product details. (name,price,etc) (/product/{id})

# ###############################
# API Schema
# ###############################
info:
  description: API Docs - Catalog (Product, Category)
  title: Catalog (Product, Category)
  version: ''
openapi: 3.0.0
paths:
  /api/category/:
    get:
      operationId: category_list
      tags:
      - category
    post:
      operationId: category_create
      tags:
      - category
  /api/category/{id}/:
    delete:
      operationId: category_delete
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this category.
          title: id
          type: integer
      tags:
      - category
    get:
      operationId: category_read
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this category.
          title: id
          type: integer
      tags:
      - category
    patch:
      operationId: category_partial_update
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this category.
          title: id
          type: integer
      tags:
      - category
    put:
      operationId: category_update
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this category.
          title: id
          type: integer
      tags:
      - category
  /api/category/{id}/product/:
    get:
      operationId: category_product
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this category.
          title: id
          type: integer
      tags:
      - category
  /api/product/:
    get:
      operationId: product_list
      tags:
      - product
    post:
      operationId: product_create
      tags:
      - product
  /api/product/{id}/:
    delete:
      operationId: product_delete
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this product.
          title: id
          type: integer
      tags:
      - product
    get:
      operationId: product_read
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this product.
          title: id
          type: integer
      tags:
      - product
    patch:
      operationId: product_partial_update
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this product.
          title: id
          type: integer
      tags:
      - product
    put:
      operationId: product_update
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this product.
          title: id
          type: integer
      tags:
      - product
  /api/product/{id}/category/:
    get:
      operationId: product_category
      parameters:
      - in: path
        name: id
        required: true
        schema:
          description: A unique integer value identifying this product.
          title: id
          type: integer
      tags:
      - product
servers:
- url: http://127.0.0.1:8000/docs/
    
