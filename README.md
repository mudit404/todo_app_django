# To-Do App - Django Project

This is a simple **To-Do List application** built using **Django** and **Django Rest Framework (DRF)**. The project includes both a web-based front-end interface (admin panel) and a RESTful API to manage tasks. It features user authentication, task management, and deployment to **Render**.

---

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Setup and Installation](#setup-and-installation)
4. [Running the Application Locally](#running-the-application-locally)
5. [Deploying to Render](#deploying-to-render)
6. [API Endpoints](#api-endpoints)
7. [CI/CD with GitHub Actions](#cicd-with-github-actions)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)

---

## Features

- **User Authentication**: Basic authentication to secure the API and admin panel.
- **CRUD Operations**: Create, Read, Update, and Delete tasks using Django's admin panel or API.
- **Tags**: Support for adding tags to tasks. Multiple tags can be assigned to the same task.
- **Status Management**: Track tasks with status options: OPEN, WORKING, PENDING REVIEW, COMPLETED, OVERDUE, CANCELLED.
- **Deployment**: Deployed on **Render** for public access.
- **Automated CI/CD**: GitHub Actions for continuous integration and deployment.

---

## Technology Stack

- **Backend**: 
  - Python 3.11+
  - Django 4.2.7+
  - Django Rest Framework 3.14.0+
  - Gunicorn for deployment

- **Testing**:
  - Pytest
  - Django Test Framework
  - Coverage

- **CI/CD**:
  - GitHub Actions for automated testing, linting, and deployment

- **Hosting**:
  - Render for cloud hosting

---

## Setup and Installation

To set up the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/mudit404/todo_app_django.git
cd todo_app_django
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure the Database
Set up the database by running the migrations:

```bash
python manage.py migrate
```
### 5. Create a Superuser
To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```
### 6. Run the Development Server
Start the server:

```bash
python manage.py runserver
```
Your application should now be available at http://127.0.0.1:8000/.

Running the Application Locally
To run the Django development server locally, use the following command:

```bash
python manage.py runserver
```
Django Admin: To access the Django admin panel, visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Deploying to Render
1. Push Your Code to GitHub
Make sure your code is pushed to a GitHub repository.

2. Create a New Web Service on Render
Visit Render and create a new web service.
Connect your GitHub repository and select the Django app.
3. Set the Start Command
In the Start Command field on Render, set the following to start the app with Gunicorn:

```bash
gunicorn todo_project.wsgi:application
```
4. Set up the Environment
Ensure that all environment variables, like database settings and secrets, are properly set in Render. Also, make sure that ALLOWED_HOSTS in settings.py is set to include the Render domain (e.g., 'todo-app-django.onrender.com').

5. Deploy
Render will automatically deploy the app after configuration.

API Endpoints
Base URL: https://your-render-domain.onrender.com/api/

Endpoints:
GET /todos/: Retrieve all tasks.
GET /todos/{id}/: Retrieve a specific task by ID.
POST /todos/: Create a new task.
PATCH /todos/{id}/: Update an existing task.
DELETE /todos/{id}/: Delete a task.
Authentication:
Basic authentication is required for all API endpoints. Use the credentials of the superuser or regular user.

CI/CD with GitHub Actions
This project uses GitHub Actions to automate testing, linting, and deployment:

Tests: Runs unit tests, integration tests, and coverage checks on every push.
Linting: Uses flake8 and black to check for style issues and enforce code formatting.
Deployment: When changes are pushed to the main branch, the app is automatically deployed to Render.
GitHub Actions Configuration:
The workflow file is located at .github/workflows/ci.yml and contains the following steps:

Set up Python and install dependencies.
Run the tests with pytest and upload a coverage report.
Run linting with flake8 and black.
Testing
Unit Tests
To run unit tests, use the following command:

```bash
pytest --cov
```
This will run all tests and generate a coverage report.
<img width="1020" alt="image" src="https://github.com/user-attachments/assets/b8f080a6-c896-4ff8-b8fc-5b848333f6a4">


End-to-End Tests:
The following scenarios are covered in the E2E tests:

Create a to-do item.
View all to-do items.
Update a to-do item.
Delete a to-do item.
You can add more scenarios based on your app's features.

Troubleshooting
1. 404 Errors for /todos/:
Ensure that the URL pattern for /todos/ is defined correctly in todo_app/urls.py and included in todo_project/urls.py.

2. Invalid HTTP_HOST Header:
Add the Render domain (todo-app-django.onrender.com) to the ALLOWED_HOSTS setting in settings.py.

3. Gunicorn Not Starting:
If the server doesn't start properly, check the logs on Render for any missing dependencies or configuration errors. Ensure gunicorn is included in your requirements.txt.

4. Missing Database Tables:
If you see errors related to missing tables, run:

bash
Copy code
python manage.py migrate
to apply migrations and set up the database schema.

Conclusion
This is a simple yet robust To-Do app built with Django. It offers basic functionality for managing tasks and includes an API for programmatic access. The app is deployed to Render, with automated CI/CD using GitHub Actions to streamline testing and deployment.
