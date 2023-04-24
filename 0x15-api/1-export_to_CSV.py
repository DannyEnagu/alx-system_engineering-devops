#!/usr/bin/python3
"""Export data in the CSV format.
   The module Takes in a user id, sends a request to an API
   and saves the response as USER_ID.csv (user ID dot csv)
"""
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
            file_name = "{}.csv".format(user_id)
            with open(file_name, 'w') as fs:
                for todo in todos.json():
                    row = '"{}","{}","{}","{}"\n'.format(
                           user_id,
                           username,
                           todo.get('completed'),
                           todo.get('title'))
                    fs.write(row)
