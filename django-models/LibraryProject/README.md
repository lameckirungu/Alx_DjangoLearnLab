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
#0. Introduction to Django Development Environment Setup
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

Tasks
-----
#0. Implementing Advanced Model Relationships in Django
-----------

 Objective:
 ---
Master Django's ORM capabilities by creating a set of models that demonstrate the use of `ForeignKey`, `ManyToMany` and `OneToOne` relationships. This task will help me understand how to model complex data relationships in a Django project effectively.

Task Description:
-----------------
- Duplicate the previous project directory `Introduction_to_Django`, rename it to `django-models` and add a new app named `relationship_app` where you'll define models that showcase complex relationships between entities using `ForeignKey`, `ManyToMany` and `OneToOne` fields.
- Implement Sample Queries: Prepare a python script `query_samples.py` in the `relationship_app` directory. This script should contain the query for each of the following relationships:
    - Query all books by aspecific author
    - List all books in a library.
    - Retrieve the librarian for a library.

#1 Django Views and URL configurration
---
Objective
---
Develop proficiency in creating both function-based and class-based views in Django, and configuring URL patterns to handle web requests effectively. This task will help you understand different ways to define views and manage URL routing in Django.

Task Description
---
In your existing Django project, enhance the `relationship_app` by adding new views that display information about books and libraries. Implement both function-based and class-based views to handle these displays and configure the URL patterns to route these views correctly.

Steps:
---
#### Implement Function-based View:
- Create a function-based view in `relationship_app/views.py` that lists all books stored in the database.
This view should render a simple text list of book titles and their authors.

#### Implement Class-based View:

- Create a class-based view in `relationship_app/views.py` that displays details for a specific library, listing all books available in that library.
Utilize Django’s ListView or DetailView to structure this class-based view.

#### Configure URL Patterns:

- Edit `relationship_app/urls.py` to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

#### Create Templates (Optional for Display):

- For a more structured output, using the code below as templates for each view to render the information in HTML format instead of plain text.


References
----------
- Official Django documentation: https://docs.djangoproject.com/

Enjoy building with Django!