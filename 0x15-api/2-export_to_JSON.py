#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/todos'
    id = sys.argv[1]
    username = requests.get(url).json()
    
    task = requests.get()
    