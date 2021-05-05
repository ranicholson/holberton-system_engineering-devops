#!/usr/bin/python3
"""Script to use REST API to gather information"""

import json
import requests
import sys

if __name__ == "__main__":
    url_target = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url_target + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        for user in users:
            ulist = []
            USER_ID = user.get("id")
            tasklist = requests.get(url_target + "todos",
                                     params={"userId": USER_ID}).json()
            for task in tasklist:
                ulist.append({"username": user.get("username"),
                             "task": task.get("title"),
                              "completed": task.get("completed")})
            jdict = {USER_ID: ulist}
            json.dump(jdict, jsonfile)
