#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the CSV format.
Usage: python3 1-export_to_CSV.py 2"""

from sys import argv
import csv
import requests

if __name__ == "__main__":

    user_id = argv[1]
    url_1 = """
    https://jsonplaceholder.typicode.com/users/{}""".format(user_id)

    url_2 = """
    https://jsonplaceholder.typicode.com/todos/?userId={}""".format(user_id)

    response_user = requests.get(url_1)
    response_task = requests.get(url_2)

    dict_user = response_user.json()
    list_tasks = response_task.json()

    user_name = dict_user.get("username")
    new_list_dict = []
    for task_dict in list_tasks:
        new_dict = {}
        new_dict["user_id"] = user_id
        new_dict["username"] = user_name
        new_dict["completed"] = task_dict.get("completed")
        new_dict["title"] = task_dict.get("title")
        new_list_dict.append(new_dict)

    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='', encoding="utf-8") as csv_file:

        dict_writer = csv.DictWriter(
            csv_file,
            new_list_dict[0].keys(),
            quoting=csv.QUOTE_ALL)
        # The following line is the header
        # dict_writer.writeheader()
        dict_writer.writerows(new_list_dict)
