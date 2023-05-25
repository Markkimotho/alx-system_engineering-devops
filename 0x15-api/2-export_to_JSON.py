#!/usr/bin/python3
"""Request employee ID from API
This script retrieves employee information and tasks
done from an API based on the provided employee ID.
It stores the information retrieved in a json file.

Usage: python3 script_name.py employee_id
       ./script_name.py employee_id
"""


import json
import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com/'


def request(resource, params=None):
    """Function that returns data in json format
    from and API"""
    url = BASE_URL + resource
    response = requests.get(url, params=params)
    data = response.json()
    return data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID.")
        sys.exit(1)

    employee_id = sys.argv[1]
    user = request('users', {'id': employee_id})
    tasks = request('todos', {'userId': employee_id})
    tasks_completed = [task for task in tasks if task['completed']]

    employee_name = user[0]['name']
    employee_user_name = user[0]['username']
    total_tasks = len(tasks)
    completed_tasks = len(tasks_completed)

    json_file_path = f'{employee_id}.json'
    json_data = {
            f'{employee_id}': [
                {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': employee_user_name
                }
                for task in tasks
                ]
            }

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)

    print(f'Employee tasks have been exported to {json_file_path}')
