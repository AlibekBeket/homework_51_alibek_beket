import json
from os import path


def file_check(path_file: str):
    if not path.isfile(path_file):
        with open(path_file, 'w') as file:
            json.dump({}, file)


def file_read(path_file: str):
    with open(path_file, 'r') as json_file:
        car_list = json.load(json_file)
    return car_list


def file_update(path_file: str, new_dict: dict):
    with open(path_file, 'w') as file:
        json.dump(new_dict, file, indent=4)
