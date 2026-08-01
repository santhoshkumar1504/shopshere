# 🛒 Django E-Commerce Web Application

A full-stack **E-Commerce Web Application** built with **Django**, enabling users to browse products, manage shopping carts, place orders, and perform secure user authentication. The application includes an admin panel for managing categories, products, customers, and orders.

---

# 🚀 Features

### 👤 User Features

* User Registration & Login
* Secure Authentication
* Browse Products by Category
* Product Search
* Product Details Page
* Add to Cart
* Update Cart Quantity
* Remove Items from Cart
* Checkout Process
* Place Orders
* Order History
* Responsive User Interface

### 🛠️ Admin Features

* Admin Dashboard
* Manage Categories
* Add/Edit/Delete Products
* Upload Product Images
* Manage Customers
* Manage Orders
* Update Order Status

---

# 🏗️ Tech Stack

### Backend

* Python
* Django
* Django ORM

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* SQLite 

### Tools

* Git
* GitHub
* Render (Deployment)
* VS Code

---

# 📁 Project Structure

```text
shopsphere/
│
├── auth_user/
├── base/
├── cart/
├── order/
├── product/
├── media/
├── static/
├── templates/
│
├── shopsphere/
│   ├── settings.py
│   ├── __init__.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/santhoshkumar1504/shopshere.git
```

Move into the project directory

Create a virtual environment

```bash
python -m venv myenv
```

Activate the virtual environment

### Windows

```bash
myenv\Scripts\activate
```

### macOS/Linux

```bash
source myenv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

Open your browser

```text
http://127.0.0.1:8000/
```

---

# 🌐 Deployment

This project is configured for deployment on **Render**.

Build Command

```bash
./build.sh
```

Start Command

```bash
gunicorn ecommerce.wsgi
```

---

# 🔐 Environment Variables

Create the following environment variables for production.

```text
SECRET_KEY=your_secret_key

DEBUG=False

DATABASE_URL=your_postgresql_database_url
```

---

# 📷 Media & Static Files

### Static Files

```text
/static/
```

Used for:

* CSS
* JavaScript
* Icons
* Bootstrap Assets

### Media Files

```text
/media/
```

Used for:

* Category Images
* Product Images

> **Note:** For production deployments, use a cloud storage service such as Cloudinary or Amazon S3 for uploaded media files instead of storing them on the local filesystem.

---

# 📊 Database Models

### Category

* Category Name
* Category Image
* Created Date

### Product

* Product Name
* Description
* Price
* Stock
* Availability
* Product Image
* Category

### Cart

* User
* Product
* Quantity

### Order

* Customer
* Products
* Quantity
* Order Status
* Order Date

# 📌 Future Enhancements

* Wishlist
* Product Reviews & Ratings
* Online Payment Integration
* Order Tracking
* Email Notifications
* Product Recommendations
* Inventory Management
* Coupon & Discount System

---

# 👨‍💻 Author

**SanthoshKumar**

* MCA Graduate
* Python Full Stack Developer
* Django Developer

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
