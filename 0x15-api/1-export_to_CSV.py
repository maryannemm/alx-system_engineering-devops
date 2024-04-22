#!/usr/bin/python3
"""
Script to export data in CSV format
"""
import csv
import requests
import sys


def export_to_csv(user_id):
    """
    Exports data in CSV format
    """
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response_users = requests.get(url_users)
    user = response_users.json()
    username = user.get('username')

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    filename = '{}.csv'.format(user_id)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for todo in todos:
            task_completed_status = todo.get('completed')
            task_title = todo.get('title')
            writer.writerow([user_id, username, task_completed_status, task_title])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)
    user_id = sys.argv[1]
    export_to_csv(user_id)

