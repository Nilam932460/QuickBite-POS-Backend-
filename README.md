Restaurant Sales API

A simple Django-based REST API for managing restaurant sales data. This API provides endpoints for managing menu items, orders, and calculating average daily sales for each of the last 4 weekdays based on completed orders.

Tech Stack

- **Backend Framework**: Django
- **REST Framework**: Django REST Framework (DRF)
- **Database**: SQLite (default), can be configured for PostgreSQL or MySQL
- **Other Libraries**: 
  - `djangorestframework`
  - `django`


Features

- **MenuItem Management**: Add, update .
- **Order Management**: Place, update, and view orders.
- **Sales Analysis**: Fetch average daily sales for each of the last 4 weekdays.
- **Admin Panel**: Full CRUD for managing MenuItems, Orders, and OrderItems via the Django admin panel.

Setup Instructions
1. Clone the repository
Clone this project to your local machine using the following command:

```bash
git clone https://github.com/Nilam932460/QuickBite-POS-Backend-.git
cd QuickBite-POS-Backend-
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/

Available Endpoints
List Available Menu Items:
GET /menu-items/

Place an Order:
POST /place-order/

List All Orders:
GET /orders/

Update Order Status:
PATCH /orders/{order_id}/update-status/

Average Sales Per Day:
GET /average-weekday-sales/

Testing the API

