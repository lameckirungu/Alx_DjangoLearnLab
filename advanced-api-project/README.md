# Advanced API Development with DRF

In this project, I expand my skills in API development by working on advanced concepts such as custom serializers, custom views, filtering, searching, orddering, and testing.

## Learning Objectives

By the end of the project, I will be able to:

1. **Set up a new Django project with Custom Serializers in DRF**
    - Initiate a new Django project tailored for advanced API development.
    - Create custom serializers to handle complex data structures and nested relationships.
2. **Build Custom Views and Generic Views in DRF**
    - Construct custom views and utilize generic views to handle specific use cases and streamline API development.
3. **Implement Filtering, Searching, and Ordering in DRF**
    - Enhance the usability and functionality of your API by adding filtering, seraching and ordering capabilities.
4. **Write Unit Tests for DRF APIs**
    - Develop and execute comprehensive unit tests to ensure the integrity of your API endpoints and the correctness of response data and status codes.

## **Tasks**

> _0. Setting up a New Django Project with Custom Serializers in DRF_

### Description

This task involves setting up a new Django project from scratch, installing Django REST Framework, and configuring a clean environment to develop an API that utilizes custom serializers, including handling nested objects and implementing data validation.

### _Action Items_

**_Step 1_: Install Django and DRF**

* Create `advanced-api-project` directory, then create a new Django project named `advanced-api-project` using the following command: `django-admin startproject advanced-api-project` . This ensures that Django initializes the project without creating an additional nested folder.
* Inside the project, create a new Django app named `api`.

**_Step 2_: Configure the Project**

- In `settings.py`:
    - Add `rest_framework` to `INSTALLED_APPS` 
    - Ensure the project is set to use Django’s default SQLite database for simplicity, or configure another database if preferred.  

**_step 3_: Define Data Models**

- Create two models, `Author` and `Book` in `api/models.py`.
- The Author model should have the following fields:
    - `name`: a string field to store the author’s name.
- The Book model should have the following fields:
    - `title`: a string field for the book’s title.
    - `publication_year`: an integer field for the year the book was published.
    - `author`: a foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books.

**_Step 4_: Create Custom Serializers**

- Create a `BookSerializer` that serializes all fields of the `Book` model.
- Create an `AuthorSerializer` that includes:
    - The `name` field.
- A nested `BookSerializer` to serialize the related books dynamically.

Validation Requirements:

- Add custom validation to the `BookSerializer` to ensure the `publication_year` is not in the future.

**_Step 5_: Document Your Model and Serializer Setup**

- In the `models.py` and `serializers.py`, add detailed comments explaining the purpose of each model and serializer.
- Describe how the relationship between `Author` and `Book` is handled in your serializers.

** _Step 6_: Implement and Test**

- Use Django admin or the django shell to manually test creating, retreiving, and serializing `Author` and `Book` instances to ensure serializers work as expected.