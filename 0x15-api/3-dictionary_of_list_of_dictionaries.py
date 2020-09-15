#!/usr/bin/python3
""" Export data in the JSON format."""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    url_1 = "https://jsonplaceholder.typicode.com/todos/"
    all_task = requests.get(url_1).json()
    user_id = all_task[0].get("userId")

    url_2 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url_2).json()

    list_dict = {}
    list_done_tasks = []

    for task in all_task:

        if task.get("userId") != user_id:

            url_2 = "https://jsonplaceholder.typicode.com/users/{}".format(
                task.get("userId"))
            user = requests.get(url_2).json()

            list_dict[user_id] = list_done_tasks
            list_done_tasks = []

        new_dict = {
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        list_done_tasks.append(new_dict)
        user_id = task.get("userId")

    list_dict[user_id] = list_done_tasks
    filename = "todo_all_employees.json".format(user_id)
    with open(filename, 'w', encoding="utf-8") as file:
        json_str = json.dumps(list_dict)
        file.write(json_str)
