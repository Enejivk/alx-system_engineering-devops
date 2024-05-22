#!/usr/bin/python3
"""Saving the file in json formate"""

import json
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    username = requests.get(user_url).json().get('username')
    tasks = requests.get(todo_url).json()

    user_task = []
    for task in tasks:
        if task.get('userId') == id:
            user_task.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username})
    dictionary = {id: user_task}
    with open('{}.json'.format(id), 'w') as file:
        json.dump(dictionary, file)
