**Project Name: Django Product API**

**Description:** This project utilizes Django Rest Framework (DRF) to create a RESTful API for managing products. It includes functionalities to create, retrieve, update, and delete products, as well as listing and detailed information endpoints. The product model consists of fields for name, price, inventory, and category, with category being a separate model linked to the product.

**Installation:** 1. Clone the repository: `git clone Aleksandre16/Restproject` 2. Navigate to the project directory: `cd django-product-api` 3. Install dependencies: `pip install -r requirements.txt` 4. Apply database migrations: `python manage.py migrate` 5. Run the development server: `python manage.py runserver`

**Endpoints:** - **Create Endpoint:** - URL: `/api/products/` - Method: POST - Creates a new product with the provided data. - **Detailed Info Endpoint:** - URL: `/api/products/<product_id>/` - Method: GET - Retrieves detailed information about a specific product. - **Product Listing:** - URL: `/api/products/`
