#!/usr/bin/python3
""" Export data in the JSON format.
Records all tasks that are owned by this employee"""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(
            user_id)

        url_2 = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
            user_id)

        response_user = requests.get(url_1)
        response_task = requests.get(url_2)

        dict_user = response_user.json()
        list_tasks = response_task.json()

        list_dict = {}
        list_done_tasks = []

        for task_dict in list_tasks:
            new_dict = {
                "task": task_dict.get("title"),
                "completed": task_dict.get("completed"),
                "username": dict_user.get("username")
            }
            list_done_tasks.append(new_dict)

        list_dict[user_id] = list_done_tasks

        filename = "{}.json".format(user_id)
        with open(filename, 'w', encoding="utf-8") as file:
            json_str = json.dumps(list_dict)
            file.write(json_str)
