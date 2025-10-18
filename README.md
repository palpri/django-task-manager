# Django Task Manager API

A RESTful API for a simple task manager application using Django. The API allow users to perform basic CRUD operations on tasks and include user authentication.

## ✨ Key Features


- **RESTful API:** Fully REST-compliant API endpoints for managing tasks.
- **Task CRUD Operations:** 
  - Create, Read, Update, and Delete tasks.
- **User Authentication:** 
  - Users can register, log in, and authenticate API requests.
- **Filtering & Sorting (Optional):** 
  - Filter tasks by completion status or sort by creation date.
- **Validation:** 
  - User authentication using JWT (JSON Web Token)
- **Pagination:** 
  - Pagination has implemented
- **Swagger API Documentation:** 
- **Unit tests with coverage support:** 

## ⚙️ Tech Stack

| Layer | Tool |
|-------|------|
| Framework | Django 5.x |
| API Layer | Django REST Framework |
| Authentication | JWT via`djangorestframework-simplejwt` |
| Filtering | `django-filter` |
| Documentation | `drf-yasg` (Swagger UI / ReDoc) |
| Database | SQLite (default) |
| Testing | Django’s `unittest` + DRF Test Client |

## 🚀 Quick Start

### Environment Setup

```bash
# Clone and setup
git clone <repository-url>
cd django-task-manager

#create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

#install dependencies
pip install -r requirements.txt

#apply migrations
python manage.py migrate

#start the server
python manage.py runserver  # Django


```

## 📁 Project Structure

```text

django-task-manager/
├── manage.py
├── requirements.txt
├── taskmanager/ # project package 
│         ├──  __init__.py
│         ├── settings.py
│         ├── urls.py
│         └── urls.py
├── tasks/ 
│     ├── migrations/
│     ├── __init__.py
│     ├── admin.py
│     ├── apps.py
│     ├── models.py  #Task model
│     ├── serializers.py
│     ├── views.py  #CRUD logic
│     ├── urls.py
│     └── tests.py
└── users/ # app for registration/login
│     ├── __init__.py
│     ├── serializers.py
│     ├── views.py
│     ├── urls.py
│     └── tests.py
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore patterns
└── README.md                       # This file

