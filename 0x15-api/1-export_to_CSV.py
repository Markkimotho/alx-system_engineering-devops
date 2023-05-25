#!/usr/bin/python3
"""Request employee ID from API
This script retrieves employee information and tasks
done from an API based on the provided employee ID.
It stores the information retrieved in a csv file.

Usage: python3 script_name.py employee_id
       ./script_name.py employee_id
"""


import csv
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

    csv_file_path = f'{employee_id}.csv'
    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id,
                            employee_user_name,
                            task['completed'],
                            task['title']])
    print(f'Employee tasks have been exported to {csv_file_path}')
