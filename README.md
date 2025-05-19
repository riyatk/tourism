# Tour Packages Management System

A web-based Tour Package Management System built with Django and SQLite. This project allows vendors to create and manage tour packages, users to browse and book them, and administrators to approve vendor submissions. Built as part of an online course to learn full-stack development with Django.

## Features

- Vendor registration and login
- Admin approval for newly created packages
- Tour package creation with auto-expiry feature
- SQLite for database management (default in development)
- Celery integration for automatic expiration of packages
- User interface to browse active tour packages
- Admin dashboard to manage users and packages

## Technologies Used

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, CSS (templates for styling)
- Task Queue: Celery with Redis (for auto-expiry tasks)
- Others: Django Admin, Django ORM

## Setup Instructions

To run this project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/riyatk/tourism.git
   cd tourism
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Run the server**
   ```bash
   python manage.py runserver   

## Project Structure

tourism/
├── manage.py
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/
│   └── ...
├── static/
├── db.sqlite3
└── ...

## License
This project is for educational purposes. No commercial license is applied.
   

