#!/usr/bin/python3
"""Script to use REST API to gather information"""

import json
import requests
import sys

if __name__ == "__main__":
    url_target = "https://jsonplaceholder.typicode.com/"
    USER_ID = sys.argv[1]
    employee = requests.get(url_target + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url_target + "todos", params={
                        "userId": sys.argv[1]}).json()
    USERNAME = employee.get("name")

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        for todo in tasks:
            json.dump({USER_ID: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": USERNAME
                }]}, jsonfile)
