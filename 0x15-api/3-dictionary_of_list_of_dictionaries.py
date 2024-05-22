#!/usr/bin/python3
"""Getting all users todo list"""

import json
import requests

if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(user_url).json()
    todo = requests.get(todo_url).json()
    dictionary = {}
    for user in users:
        user_task = []
        for task in todo:
            if task.get('userId') == user.get('id'):
                user_task.append(
                    {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": user.get('username')})
        dictionary[user.get('id')] = user_task
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
