#!/usr/bin/python3
"""Export the content as json"""

import requests
import csv
import sys

if __name__ == '__main__':
    id = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    username = requests.get(user_url).json().get('username')
    tasks = requests.get(todo_url).json()
    with open('2.csv', 'w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get('userId') == id:
                csv_writer.writerow([task.get('userId'), username,
                                    task.get('completed'), task.get('title')])
