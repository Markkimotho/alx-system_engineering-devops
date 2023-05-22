#!/usr/bin/python3
"""Module that requests employee ID from API
and returns information about his/her TODO list progress
"""

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
    total_tasks = len(tasks)
    completed_tasks = len(tasks_completed)

    print('Employee {} is done with tasks ({}/{}):'.format(employee_name,
                                                           completed_tasks,
                                                           total_tasks))
    for task in tasks_completed:
        print(f'     {task["title"]}')
