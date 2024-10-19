# Django Application

## Introduction
This Django application provides a basic implementation of user and role management. It includes CRUD operations for users and roles, user authentication (login/signup), access module management, bulk user updates, and search functionality within the list APIs.

## Features
- **CRUD Operations**: Manage users and roles with create, read, update, and delete functionalities.
- **User Authentication**: Login and signup APIs for user authentication.
- **Access Module Management**: Update, remove, and check user access to specific modules.
- **Bulk User Updates**: Update multiple users with the same or different data in a single call.
- **Search Functionality**: Implement search in list APIs to find users or roles by specific criteria.

## Python Version
- **Python Version**: 3.8+
- **Dependencies**: The project requires the following dependencies:
  - Django
  - djangorestframework
  - djangorestframework-simplejwt

## Project Structure
- `user/` - Handles user management. Contains CRUD APIs to manage users.
- `role/` - Handles role management. Contains CRUD APIs to manage roles.

## Running the Project Locally

### Environment Setup
1. **Clone the repository**:
    ```bash
    git clone https://github.com/umangkotadiya/Scaletech.git
    cd yourproject
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

### Dependency Installation
1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Application Startup Commands
1. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

2. **Create a superuser** (for accessing the admin site):
    ```bash
    python manage.py createsuperuser
    ```

3. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

4. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:8000/`

## API Endpoints
- **Role Module**:
  - `POST /roles/`: Create a new role.
  - `GET /roles/`: Retrieve a list of roles.
  - `GET /roles/<id>/`: Retrieve a specific role by ID.
  - `PUT /roles/<id>/`: Update a role by ID.
  - `DELETE /roles/<id>/`: Delete a role by ID.
  - `POST /roles/<id>/add_access_module/`: Add an access module to a role.
  - `POST /roles/<id>/remove_access_module/`: Remove an access module from a role.

- **User Module**:
  - `POST /users/`: Create a new user.
  - `GET /users/`: Retrieve a list of users (supports search functionality).
  - `GET /users/<id>/`: Retrieve a specific user by ID.
  - `PUT /users/<id>/`: Update a user by ID.
  - `DELETE /users/<id>/`: Delete a user by ID.
  - `POST /users/login/`: Login a user and return an authentication token.
  - `PUT /users/bulk_update/`: Bulk update users' last names.

## Test Data for API Endpoints

### Login
```python
import requests

login_url = "http://127.0.0.1:8000/users/login/"
login_data = {
    "username": "harsh",
    "password": "harsh123"
}
response = requests.post(login_url, json=login_data)
print(response.json())
