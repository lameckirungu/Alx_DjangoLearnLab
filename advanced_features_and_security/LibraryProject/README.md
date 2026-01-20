Advanced Features and Security
---
This project is an extension of [../django-models]. It is designed to enhance hte learners understandign of user models, permissions, security practices, and secure communication in Django applications. Through a series of tasks, the learner will implement custom user models, manage permissions and groups, apply security best practices, and configure HTTPS and secure redirects.

Learning Objectives
---
By the end of the project, the learner should be able to:
1. Implement a Custom User model in Django:
    - Customize Django User's model to include additional fields and functionality.
    - Configure settings and integrate the custom user model into the Django admin.
2. Manager Permissions and Groups in Django:
    - Implement and manage permissions and groups to control access to various parts of your application.
    - Develop views that enforce these permissions and document the setup process.
3. Apply Security Best Practices in Django:
    - Configure Django settings to prevent security vulnerabilities and ensure data privacy.
    - Protect views and templates against common security threates such as CSRF, XSS, and SQL injection
4. Implement HTTPS and Secure Redirects in Django:
    - Configure Django to handle secure HTTPS connections and enforce HTTPS redirects.
    - Adjust settings for secure cookies and implement secure headers against various attacks.


## **Tasks**
_**#0. Implementing a Custom User Model in Django**_

### Objective
---
Customize Django's user model to suit the specific needs of your application, demonstrating an understanding of Django's authentication system.

### Task Description:
---
Replace Django's default user model with a custom user model that includes additional fields and functionality. It's a critical feature for applications that require user attributes beyond Django's built-in user model

Step 1: Set up the Custom User Model
---
- Duplicate the previous Django project `django-models` and rename it to `advanced_features_and_security`
- Create a custom user model by extending `AbstractUser`, adding custom fields that are relevant to your application's needs. Add the following fields:
    - `date_of_birth`(A date field)
    - `profile_photo`(An Image field)

Step 2: Update settings to use the custom user model
---
Configure Django to use this custom user model fo all user-related functionalities.
- Settings Configuration: In your project's `settings.py`, set the `AUTH_USER_MODEL` to point to your new custom user model.

Step 3: Create User Manager for Custom User Model
---
Implement a custom user manager that handles user creation and queries, ensuring it can manager the added fields effectively.
- Custom Manager Functions to Implement:
    - `create_user`: Ensure it handles the new fields correctly.
    - `create_superuser`: Ensure administrative users can still be created with the required fields.

Step 4: Integrate the Custom User Model into Admin
---
Modify the Django admin to support the custom user model, ensuring that administrators can manager uwers effectively through the Django admin interface.
- Admin Modifications Required:
    - Define a custom `ModelAdmin` class that includes configurations for the additional fields in your user model

Step 5: Update your Application to use the Custom User Model
---
Adjust any part of your application that references the user model to use sthe new custom model.
- Application Updates:
    - Update all foreign keys or user model references in your other models to use the custom user model 