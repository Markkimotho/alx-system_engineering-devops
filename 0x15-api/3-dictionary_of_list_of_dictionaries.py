#!/usr/bin/python3
"""Request employee ID from API
This script retrieves all employee information and tasks
done from an API.
It stores the information retrieved in a json file.

Usage: python3 script_name.py
       ./script_name.py
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

    users = request('users')
    tasks = request('todos')

    tasks_by_user = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in tasks if task['userId'] == user_id]
        user_task_data = [
                {
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                }
                for task in user_tasks
            ]

        tasks_by_user[user_id] = user_task_data

    json_data = json.dumps(tasks_by_user)

    json_file_path = 'todo_all_employees.json'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
