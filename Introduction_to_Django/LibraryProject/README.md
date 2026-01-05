# LibraryProject — Introduction to Django

Objective
--------
Gain familiarity with Django by setting up a development environment and creating a basic Django project. This README shows the minimal steps to install Django, create the project, run the development server, and inspect the default project layout.

Prerequisites
-------------
- Python 3.8 or newer
- pip

Optional (recommended)
----------------------
Create and activate a virtual environment before installing packages:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install Django
--------------
Install Django into your (optional) virtual environment:

```bash
pip install django
```

## Tasks
#### 0. Introduction to Django Development Environment Setup
------------------
Create a new Django project named `LibraryProject`:

```bash
django-admin startproject LibraryProject
```

Run the development server
--------------------------
Change into the project directory and start the dev server:

```bash
cd LibraryProject
python manage.py runserver
```

Open a browser at http://127.0.0.1:8000/ to see the default Django welcome page.

Project structure
----------------------------------
- `manage.py`: Command-line utility for interacting with this Django project (migrations, runserver, etc.).
- `LibraryProject/settings.py`: Central configuration for your project (installed apps, middleware, databases, static files).
- `LibraryProject/urls.py`: URL declarations that map URLs to views — the project's top-level routing table.
- `LibraryProject/wsgi.py` / `LibraryProject/asgi.py`: Entry points for WSGI/ASGI-compatible web servers.

Next steps
----------
- Create an app with `python manage.py startapp <appname>`.
- Add the app to `INSTALLED_APPS` in `settings.py`.
- Create models, run migrations, and build views/templates.

References
----------
- Official Django documentation: https://docs.djangoproject.com/

Enjoy building with Django!