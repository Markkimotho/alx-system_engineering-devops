#!/usr/bin/python3
"""Request employee ID from API
This script retrieves employee information and tasks
done from an API based on the provided employee ID.It then
displays the completed tasks for the specified employee.

Usage: python3 script_name.py employee_id
       ./script_name.py employee_id
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
    tasks_completed = [task for task in tasks if task['completed'] is True]

    employee_name = user[0]['name']
    total_tasks = len(tasks)
    completed_tasks = len(tasks_completed)

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          completed_tasks,
                                                          total_tasks))
    for task in tasks_completed:
        print(f'\t {task["title"]}')
