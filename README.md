# Django Backend 

### Usage 
1. the use of venv is recommended
    ```
    pip install requirements.txt 
    # or pip3 install requirements.txt 
    ```

2. start server 
    ```
    cd backend 
    python manage.py runserver
    # or python3 manage.py runserver
    ```
### Remark 
~none~
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