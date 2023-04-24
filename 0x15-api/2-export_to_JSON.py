#!/usr/bin/python3
"""Export data in the JSON format.
   The module Takes in a user id, sends a request to an API
   and saves the response as USER_ID.ison (user ID dot json)
"""
import json
import requests
import sys


URL = "https://jsonplaceholder.typicode.com"
"""Link to API"""


if __name__ == "__main__":
    if (len(sys.argv) > 1 and
            isinstance(int(sys.argv[1]), int)):
        user_id = int(sys.argv[1])
        user = requests.get("{}/users/{}".format(URL, user_id))
        todos = requests.get("{}/user/{}/todos/".format(URL, user_id))
        if (user.status_code == requests.codes.ok and
                todos.status_code == requests.codes.ok):
            username = user.json().get('username')
            file_name = "{}.json".format(user_id)
            user_data = {}
            tasks = []
            for todo in todos.json():
                task = {}
                task['task'] = todo.get('title')
                task['completed'] = todo.get('completed')
                task['username'] = username
                tasks.append(task)
            user_data[user_id] = tasks

            with open(file_name, 'w') as fs:
                json.dump(user_data, fs)
