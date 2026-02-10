# ALX Django Learning Lab

A comprehensive collection of Django projects and exercises developed as part of the ALX Software Engineering program. This repository demonstrates progressive learning of Django web framework, from basic concepts to advanced features.

##  Overview

This repository contains multiple Django projects covering various aspects of web development with Django, including:

- Django fundamentals and project structure
- Database models and ORM
- RESTful API development
- Advanced features and security implementations

##  Repository Structure

```
Alx_DjangoLearnLab/
│
├── Introduction_to_Django/       # Getting started with Django basics
│
├── django-models/                # Database models and relationships
│
├── api_project/                  # Basic API development with Django REST Framework
│
├── advanced-api-project/         # Advanced API features and patterns
│
└── advanced_features_and_security/  # Security best practices and advanced Django features
```

## Technologies Used

- **Python** (87%) - Primary programming language
- **HTML** (13%) - Template rendering
- **Django** - Web framework
- **Django REST Framework** - API development
- **SQLite/PostgreSQL** - Database systems

##  Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/lameckirungu/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Navigate to a specific project directory and install dependencies:
```bash
cd <project-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Projects Description

### Introduction to Django
Foundational Django concepts including:
- Project setup and configuration
- URL routing and views
- Templates and static files

### Django Models
Database modeling and ORM operations:
- Model creation and relationships
- Queries and database operations
- Model managers and custom methods

### API Project
Basic REST API development:
- Setting up Django REST Framework
- Serializers and ViewSets
- API endpoints and routing

### Advanced API Project
Advanced API features:
- Authentication and permissions
- Filtering, searching, and pagination
- Custom API views and mixins

### Advanced Features and Security
Security implementations and advanced Django features:
- User authentication and authorization
- Security best practices (CSRF, XSS, SQL Injection prevention)
- Custom permissions and middleware
- Advanced Django features

## Learning Objectives

- Understand Django's MVT (Model-View-Template) architecture
- Build and manage database models with Django ORM
- Create RESTful APIs using Django REST Framework
- Implement authentication and authorization
- Apply security best practices in web development
- Deploy Django applications

##  Documentation

For more information about Django:
- [Official Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

## Contributing

This is a learning repository, but suggestions and improvements are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is part of the ALX Software Engineering program.

##  Author

**lameckirungu**
- GitHub: [@lameckirungu](https://github.com/lameckirungu)

##  Acknowledgments

- ALX Africa for the comprehensive curriculum
- The Django community for excellent documentation and resources

---

*This repository is actively maintained as part of ongoing learning and development.*
