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

**_Step 6_: Implement and Test**

- Use Django admin or the django shell to manually test creating, retreiving, and serializing `Author` and `Book` instances to ensure serializers work as expected.

> 1. _Building Custom Views and Generic Views in DRF_

### Description

Expand your `advanced_api_project` by creating and configuring custom views using DRF powerful generic views and mixins. This task will focus on efficiently handling CRUD operations and fine-tuning API beahvior to meet specific requirements.

### _Action Items_

**_Step 1_: Set Up Generic Views**

- Implement a set of generic views for the `Book` model to handle CRUD ops:
    - A `ListView` for retrieving all books.
    - A `DetailView` for retrieving a single book by ID.
    - A `CreateView` for adding a new book.
    - An `UpdateView` for modifying an existing book.
    - A `DeleteView` for removing a book.

**_Step 2_: Define URL Patterns**

- **Routing Requirements**:
    - Configure URL patterns in `api/urls` to connect to aforementioned views with specific endpoints.
    - Each view should have a unique URL path corresponding to its function

**_step 3_: Customize View Behavior**

- Customize the `CreateView` and `UpdateView` to ensure they properly nadle form submissions and data validation.
- Integrate additional fucntionalities such as permission checks or filters directly into the views usign DRF's built in features or custom methods.

**_Step 4_: Impelement Permissions**

- Apply DRF's permission classes to protect API endpoints based on user roles.
- For example, restrict `CreateView`, `UpdateView` and `DeleteView` to authenticated users only, while allowing read-only access to unauthenticated users for `ListView` and `DetailView`.

**_Step 5_: Test the Views**

- Manually test each view through tools like Postman or `curl` to ensure they behave as expected. CRUD operations and permissions.

**_Step 6_: Document the View configurations**

- Provide clear documentation in your code
- Outline any custom settings or hooks used in the views to extend or modify their default behavior.

> 2. Implementing Filtering, Searching, and Ordering in DRF

### Description

Enhance the usability and functionality of your API by implementing filtering, searching and ordering capabilities. This task focuses on providing users with the tools to easily access and manipulate data presented through your API.

### _Action Items_

**_Step 1_: Set Up Filtering**

- Integrate DRF's filtering capabilities by vairous attributes such as `title`, `author` and `publication_year`.
- Use DRF's `DjangoFilterBackend` or similar tools to set up comprehensive filtering options in your `ListView`.

**_Step 2_: Implement Search Functionality**

- **Search Setup**:
    - Enable search functionality on one or more fields of the `Book` model, such as `title` and `author`.
    - Configure the `SearchFilter` in your API to allow users to perform text searches on these fields.

**_step 3_: Configure Ordering**

- Allow users to order the results by any field of the `Book` model, particularly `title` and `publication_year`.
- Set up the `OrderingFilter` to provide front-end flexibility in sorting query results.

**_Step 4_: Update API Views**

- Adjust your `BookListView` to incorporate filtering, searching, and ordering functionalities.
- Ensure that these capabilities are clearly defined and integrated into the view logic.

**_Step 5_: Test API Functionality**

- Test the filtering, searching, and ordering features to ensure they work correctly.
- use API testing tools: postman, curl to make requests with various query parameters to evaluate how the API handles them.

**_Step 6_: Document the Implementation**

- Detail how filtering, searching, and ordering were implemented in yoru views. 
- Include examples of how to use tehse features in API requests in the project documentation or code comments.

