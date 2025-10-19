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
├── taskmanager/                                # project package 
│         ├──  __init__.py
│         ├── settings.py                       #Global project settings (apps, middleware, DB, REST config)
│         ├── utils.py                          #Custom utilities like global exception handler
│         ├── wsgi.py 
│         └── urls.py                          #Root URL routes — connects global URLs to app URLs
├── tasks/ 
│     ├── migrations/
│     ├── __init__.py
│     ├── admin.py                             #Django Admin integration for Task model
│     ├── apps.py                              #App configuration (auto-created)
│     ├── models.py                            #Database models (Task) 
│     ├── serializers.py                       #DRF serializers — convert models <-> JSON for API
│     ├── views.py                             #CRUD logic (List, Create, Update, Delete Task endpoints)
│     ├── urls.py                              #API routes for /api/tasks/, /api/tasks/{id}/ etc.
│     └── tests.py                             #Unit tests for API endpoints
└── users/ # app for registration/login
│     ├── __init__.py
│     ├── serializers.py                       #Handle register/login serializers
│     ├── views.py                             #Login/Register API logic
│     ├── urls.py                              #Auth routes (/api/register/, /api/login/)
│     └── tests.py                             #Unit tests
├── requirements.txt                           # Python dependencies list
├── .gitignore                                 # Git ignore patterns
└── README.md                                  # documentation — setup steps, API usage, test guide

```
## Check Code Coverage 

```bash
#install dependencies
pip install coverage

#Generate detailed HTML report
coverage html

#specific file test
python manage.py test users/tasks


```
## Urls of APIs

Tasks: http://127.0.0.1:8000/api/tasks/

Single task: http://127.0.0.1:8000/api/tasks/1/

Auth register: http://127.0.0.1:8000/api/auth/register/

Login: http://127.0.0.1:8000/api/auth/login/

Admin: http://127.0.0.1:8000/admin/

Swagger: http://127.0.0.1:8000/swagger/

Postman collection link:https://pri-9520449.postman.co/workspace/pri's-Workspace~0d519b28-9e3f-48b6-8490-8329f4b9b7e2/collection/44601934-88a8d2a6-12b9-4186-af1c-30594b9c78fd?action=share&creator=44601934

Collection json file-(TaskManager.postman_collection.json)

Please refer to Doc for testing of urls:https://docs.google.com/document/d/1MfjTtn6lylTEOYLm6jHLChc_HnmOgHnUaiNC9EPPlYo/edit?usp=sharing



