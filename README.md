# E-Commerce_Backend

E-Commerce Backend
Real-World Application
The e-commerce backend were builts to simulates a real-world application,  a well optimize relational database schemas. A well Built and documented APIs for frontend integration. 

## Overview
The backend system manages an e-commerce product catalog. It handles product data management, user authentication, and APIs for filtering, sorting, and pagination, simulating a real-world scenario for backend applications.

## Project Goals
CRUD APIs: Build APIs for managing products, categories, brand and user authentication.
Filtering, Sorting, Pagination: Implement robust logic for efficient product discovery.
Database Optimization: Our Database schema Design to support seamless queries.

## Technologies Used

Django: A High-level Python backend framework.

Django REST Framework: For API development.

PostgreSQL: Optimized relational database.

Cloudinary: Media/image storage solution.

JWT (SimpleJWT): Secure authentication.

Swagger / drf-yasg: API documentation.

## The backend handles:

Product catalog management (products, brands, categories).

User authentication and authorization.

Well-documented APIs to enable seamless frontend integration.

Efficient product discovery with filtering, sorting, and pagination.


## CRUD APIs

Modules to Manage (Post, Get, Put, Patch and Delete request) for products, categories and users.

Modules to Enable brands and product images integration.

logic for Filtering, Sorting, and Pagination

Efficient product discovery with advanced querying capabilities.

Database Optimization: PostgreSQL indexing for fast lookups.

Normalized relational schema for scalability.

Security & Authentication: Implementation with JWT authentication for secure access.

API Documentation: Swagger/OpenAPI for API testing and exploration.

## Project Structure
E-Commerce_Backend/
│── product_catalog/       # Core Django project settings
│── catalog/               # Product catalog app (Products, Brands, Categories)
│── userauths/             # Custom user authentication app
│── requirements.txt       # Python dependencies
│── manage.py              # Django entry point


## Installation & Setup

Clone the repository

git clone https://github.com/myusername/ecommerce-backend.git
cd ecommerce-backend


Create a virtual environment

python -m venv venv
On Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt


Set up PostgreSQL database

Create a database (e.g., ecommerce_db) in PostgreSQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Run migrations

python manage.py makemigrations
python manage.py migrate


## Create a superuser

python manage.py createsuperuser


## Run the development server

python manage.py runserver

## Media Handling using Cloudinary

Cloudinary is integrated for product image storage.

Update settings.py with your Cloudinary credentials:

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
    'FOLDER': 'product_images',
}

## Author

Ogbonna Emmanuel Ndubuisi