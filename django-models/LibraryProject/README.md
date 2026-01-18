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

#2. Implementing User Authentication in Django
---
Objective
---
Develop the ability to manager user authentication within a Django app. This task focuses on setting up user login, logout, and registration functionalities using Django's built-in authentication system.

Task Description
---
Enhance your `relationship_app` by adding user authentication features. Implement views and templates for user login, logout, and registration to demonstrate how Django mangers user sessions and permissions.

Steps:
---
1. Setup User Authentication Views:
    - Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.
2. Create Templates for Authentication:
    - Provide HTML templates for each authentication action (login, logout, and registration
3. Configure URL patterns:
    - Define URL patterns in `relationship_app/urls.py` to link to the authentication views.
4. Test Authentication Functionality:
    - Ensure that users can register, log in, and log out.

#3 Implement Role-Based Access Control in Django
---
Objective
---
Implement role-based access control within a Django applciation to manger different user roles and permissions effectively. You will extend the `User` model and create views that restrict access based on user roles.

Task Description
---
In your Django project, you will extend teh Django `User` model to include user roles and develop views that restrict access based on these roles. Your task is to set up this system by creating a new model for user profiles, definiing views with access restrictions, and configuring URL patterns.

Steps:
---
### 1. Extend the User Model with a UserProfile

- It includes a `role` field with predefined roles. 
- It is linked to Django's built-in `User` model with a one-to-one relationship.

    _Required Fields:_
    
    - `user`: 1-1 linked to Django's `User`.
    -  `role`: CharField with choices for 'Admin', 'Librarian', 'Member'

    _Automatic Creation:_
    Use Django signals to automatically create a `UserProfile` when a new user is registered.

### 2. Set up Role-Based Views:
---

Create three separate views to manage content access based on user roles:

#### _Views to Implement:_

- An Admin view that only users with the 'Admin' role can access, the name fo teh file should be `admin_view`
- A Librarian View accessible only to users identified as 'Librarians'. The file should be named `librarian_view`.
- A Member view for users with teh 'Member' role, the name of the file should be `member_view`

#### _Access Control:_
- utilize the `@user_passes_test` decorator to check the user's role before granting access to each view


### 3. Configure URL patterns:
Define URL patterns that will route to the newly create role-specific views.

### 4. Create Role-Based HTML templates:
For each role, create a HTML template to display relevant content when users access their respective views, namely:

- `admin_view.html` for Admin users.
- `librarian_view.html` for Librarians.
- `member_view.html` for Members.

### #4. Implementing Custom Permissions in Django

Objective
---
Implement custom permissions in your Django application to control access to specific actions such as adding, editing, and deleting book entries based on user roles. This task will guide you through creating permissions in the model and enforcing them in views.

Task Description:
---
In the relationship_app of your Django project, extend the existing Book model to include custom permissions. You will then update the views to enforce these permissions, ensuring that only authorized users can perform certain actions.

#### _Step 1: Extend the Book Model with Custom Permissions_
- Add custom permissions to the Book model to specify who can add, edit, or delete the entries.
- Inside the `Book` model, define a nested Meta class.
Within this Meta class, specify a permissions tuple that includes permissions like `can_add_book`, `can_change_book`, and `can_delete_book`.

#### _Step 2: Update Views to Enforce Permissions_
Adjust your views to check if a user has the necessary permissions before allowing them to perform create, update, or delete operations.
- Use Django’s `permission_required` decorator to secure views that add, edit, or delete books.
For each view, apply the corresponding permission.

#### _Step 3: Define URL patterns for Secured Views_
Ensure that the secured views are accessible through specific URLs. Set up these URLs in your `urls.py` file and ensure they are properly named for clarity.
- Create distinct paths for adding, editing, and deleting books.
- Link each path to its respective view with the appropriate permissions

### _Deliverables:_
* `models.py`: Update the Book model to include a Meta class with defined custom permissions.
* `views.py`: Implement permission checks in the views that handle book creation, modification, and deletion.
* `urls.py`: Configure and submit the URL patterns that map to the secured views.

#### Instructions for Each File:
- `models.py`: In the Book model, add a Meta class defining the custom permissions.
- `views.py`: For each action (add, edit, delete), use the `permission_required` decorator from `django.contrib.auth.decorators` to check the corresponding permission.
- `urls.py`: Define URL patterns that use the views decorated with permissions.


References
----------
- Official Django documentation: https://docs.djangoproject.com/

Enjoy building with Django!