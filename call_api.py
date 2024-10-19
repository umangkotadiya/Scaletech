import requests

BASE_URL = "http://127.0.0.1:8000"

def signup_user():
    url = f"{BASE_URL}/users/create/"
    data = {
        "username": "umang",
        "first_name": "umang",
        "last_name": "kotadiya",
        "email": "umang@gmail.com",
        "password": "umang123",
        # "role": 2
    }
    response = requests.post(url, json=data)
    print("Signup Response:", response.json())
    return response

def login_user():
    url = f"{BASE_URL}/users/login/"
    data = {
        "username": "umang",
        "password": "umang123"
    }
    response = requests.post(url, json=data)
    print("Login Response:", response.json())
    return response

def create_role(token):
    url = f"{BASE_URL}/roles/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "role_name": "Editor",
        "access_modules": ["edit", "delete"]
    }
    response = requests.post(url, json=data, headers=headers)
    print("Create Role Response:", response.json())
    return response

def list_roles(token):
    url = f"{BASE_URL}/roles/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    print("List Roles Response:", response.json())
    return response

def update_role(token, role_id):
    url = f"{BASE_URL}/roles/{role_id}/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "role_name": "Editor Updated",
        "access_modules": ["edit", "delete", "view"]
    }
    response = requests.put(url, json=data, headers=headers)
    print("Update Role Response:", response.json())
    return response

def delete_role(token, role_id):
    url = f"{BASE_URL}/roles/{role_id}/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers)
    print("Delete Role Response:", response.status_code)
    return response

def add_access_module(token, role_id, module):
    url = f"{BASE_URL}/roles/{role_id}/add_access_module/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "module": module
    }
    response = requests.post(url, json=data, headers=headers)
    print("Add Access Module Response:", response.json())
    return response

def remove_access_module(token, role_id, module):
    url = f"{BASE_URL}/roles/{role_id}/remove_access_module/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "module": module
    }
    response = requests.post(url, json=data, headers=headers)
    print("Remove Access Module Response:", response.json())
    return response

def bulk_update_users(token, user_ids, last_name):
    url = f"{BASE_URL}/users/bulk_update/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "ids": user_ids,
        "last_name": last_name
    }
    response = requests.put(url, json=data, headers=headers)
    print("Bulk Update Users Response:", response.json())
    return response

def search_users(token, query):
    url = f"{BASE_URL}/users/?search={query}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    print("Search Users Response:", response.json())
    return response

def main():
    signup_response = signup_user()
    login_response = login_user()
    if login_response.status_code == 200:
        token = login_response.json().get("access")
        print("Sucesfull to login.")
        create_role(token)
        list_roles(token)
        update_role(token, 3)
        delete_role(token, 4)
        add_access_module(token, 3, "custom")
        remove_access_module(token, 3, "custom")
        bulk_update_users(token, [7], "patel")
        search_users(token, "U")
    else:
        print("Failed to login.")

if __name__ == "__main__":
    main()
