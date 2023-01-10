"""
Implement function parse_user(output_file, *input_files) for creating file that will
contain only unique records (unique by key "name") by merging information from all input_files argument
(if we find user with already existing name from previous file we should ignore it).
Use pretty printing for writing users to json-file.


If the function cannot find input files we need to log information with error level

root - ERROR - File <file name> doesn't exist

For example:
user1.json :
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json :
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

"""

import json
import logging

logging.basicConfig(filename='Test_data/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def load_json(file):
    folder = "Test_data/"
    # folder = ""
    try:
        with open(folder + file, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f"File {file} doesn't exist")


def save_json(file, data):
    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    return file


def only_uniq(new_value: dict, uniq_values: list):
    flag = True
    for each in uniq_values:
        if new_value["name"] == each["name"]:
            flag = False
    return flag


def add_records(dct: list, uniq_values: list):
    for each in dct:
        if list(each)[0] == "name":
            if only_uniq(each, uniq_values):
                uniq_values.append(each)


def parse_user(output_file, *input_files):
    uniq_values = []
    for file in input_files:
        data = load_json(file)
        if data is not None:
            add_records(data, uniq_values)

    save_json(output_file, uniq_values)


# type your code here


if __name__ == "__main__":
    parse_user("user4.json", "user1.json", "user2.json")
    # print_file("user4.json")
    # [
    #     {
    #         "name": "Bob1",
    #         "languages": [
    #             "English",
    #             "French"
    #         ]
    #     },
    #     {
    #         "name": "Bob2",
    #         "languages": [
    #             "English",
    #             "French"
    #         ]
    #     },
    #     {
    #         "name": "Bob",
    #         "languages": [
    #             "English",
    #             "Fench"
    #         ]
    #     }
    # ]

    # parse_user("user4.json", "user_without_name.json")
    # print_file("user4.json")
