#!/usr/bin/python3
"""Script to use REST API to gather information and export in CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    url_target = "https://jsonplaceholder.typicode.com/"
    USER_ID = sys.argv[1]
    employee = requests.get(url_target + "users/{}".format(USER_ID)).json()
    tasks = requests.get(url_target + "todos", params={
                        "userId": USER_ID}).json()
    USERNAME = employee.get("username")

    with open("{}.csv".format(USER_ID), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todos in tasks:
            writer.writerow([USER_ID, USERNAME,
                            todos.get("completed"), todos.get("title")])
