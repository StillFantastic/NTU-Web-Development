# Django Backend 

### Usage 
1. the use of venv is recommended
    ```
    pip install requirements.txt 
    ```
2. migrate 
    ```
    python manage.py makemigrations
    python manage.py migrate  
    ```
3. start server 
    ```
    cd backend 
    python manage.py runserver
    ```
### Remark 
**backend/db.sqlite3 is not up to date  and will not update**
**Please migrate before runserver**
### Project structure 
```
backend/
│
├── mainSite/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── img/
│   │       └── rick-roll.jpeg
│   ├── templates/
│   │   └── myapp/
│   │       └── registration.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```