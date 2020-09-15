#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the CSV format.
Usage: python3 1-export_to_CSV.py 2"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    url_2 = "https://jsonplaceholder.typicode.com/todos".format(
        user_id)

    response_user = requests.get(url_1)
    response_task = requests.get(url_2, params={"userId": user_id})

    dict_user = response_user.json()
    list_tasks = response_task.json()

    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='', encoding="utf-8") as csv_file:
        user_name = dict_user.get("username")
        new_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # uncomenting newxt line will add a header as first row
        # new_writer.writerow(['user_id', 'username', 'completed', 'title'])
        for task_dict in list_tasks:
            new_list = []
            new_list.append(user_id)
            new_list.append(user_name)
            new_list.append(task_dict.get("completed"))
            new_list.append(task_dict.get("title"))
            new_writer.writerow(new_list)
