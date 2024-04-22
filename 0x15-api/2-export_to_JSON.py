#!/usr/bin/python3
"""
A Python script that, using a REST API, retrieves information about an employee's TODO list progress
and exports the data in JSON format.
"""

import sys
import json
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee's name and a list of dictionaries representing the employee's TODO list.
    """
    # URL of the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Sending GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Failed to retrieve data from the API.")
        sys.exit(1)

    # Extracting JSON data from the response
    todos = response.json()

    # Getting the employee's name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    return employee_name, todos

def export_to_json(employee_id, employee_name, todos):
    """
    Exports the employee's TODO list to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The username of the employee.
        todos (list): A list of dictionaries representing the employee's TODO list.
    """
    # File name
    file_name = f"{employee_id}.json"

    # Data to be written to JSON file
    data = {str(employee_id): [{"task": todo['title'], "completed": todo['completed'], "username": employee_name} for todo in todos]}

    # Writing data to JSON file
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, todos = get_employee_todo_progress(employee_id)
    export_to_json(employee_id, employee_name, todos)

