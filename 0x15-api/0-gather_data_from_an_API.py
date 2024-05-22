#!/usr/bin/python3
"""Generating todo list for a certain user and """

import requests
import sys

if __name__ == "__main__":
    total_task = 0
    completed_task = 0
    incompletely_task = 0
    task_title = []

    id = int(sys.argv[1])
    userId_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    name = requests.get(userId_url).json().get('name')
    task_respond = requests.get(todo_url).json()

    for task in task_respond:
        if task.get('userId') == id:
            total_task += 1
            if task.get('completed') is True:
                task_title.append(task.get('title'))
                completed_task += 1
            else:
                incompletely_task += 1

    print(f"Employee EMPLOYEE_NAME is done with tasks(
        {completed_task}/{total_task}): ")
    for title_task_item in task_title:
        print('\t', title_task_item)
