#!/usr/bin/python3
"""
Script to export data in JSON format
"""
import json
import requests


def export_to_json():
    """
    Exports data in JSON format
    """
    url_users = 'https://jsonplaceholder.typicode.com/users'
    response_users = requests.get(url_users)
    users = response_users.json()

    data = {}
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
        response_todos = requests.get(url_todos)
        todos = response_todos.json()

        data[user_id] = [{'username': username, 'task': todo['title'], 'completed': todo['completed']} for todo in todos]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    export_to_json()

