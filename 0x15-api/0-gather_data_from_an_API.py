#!/usr/bin/python3
"""
A Python script that, using a REST API, retrieves information about an employee's TODO list progress.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: A formatted string representing the employee's TODO list progress.
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

    # Counting completed and total tasks
    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)

    # Getting the employee's name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Formatting the output
    output = f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):\n"
    for todo in todos:
        if todo['completed']:
            output += f"\t{todo['title']}\n"

    return output

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    print(get_employee_todo_progress(employee_id))

