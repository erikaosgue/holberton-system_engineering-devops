#!/usr/bin/python3
"""Using this REST API <https://jsonplaceholder.typicode.com/>
For a given employee ID, returns information about his/her TODO list progress
Usage: python3 0-gather_data_from_an_API.py <EMPLOY ID ej: 2>"""

import requests
import sys

if __name__ == "__main__":

    emplyee_id = sys.argv[1]
    url_1 = """
    https://jsonplaceholder.typicode.com/users/{}""".format(emplyee_id)

    url_2 = """
    https://jsonplaceholder.typicode.com/todos/?userId={}""".format(emplyee_id)

    response_employee = requests.get(url_1)
    response_task = requests.get(url_2)

    dict_user = response_employee.json()
    list_task = response_task.json()

    list_done_tasks = [
        task_dict.get("title")
        for task_dict in list_task
        if task_dict.get("completed") is True
    ]

    print("Employee {} is done with tasks({}/{}):".
          format(dict_user.get("name"), len(list_done_tasks), len(list_task)))
    for task_title in list_done_tasks:
        print("\t {}".format(task_title))
