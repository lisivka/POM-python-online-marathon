"""
Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.
Make both classes JSON serializable.
Json-files represent information about student (students).

Create methods:
Student.from_json(json_file) that return Student instance from attributes from json-file;
Student.serialize_to_json(filename)
Group.serialize_to_json(list_of_groups, filename)
Group.create_group_from_file(students_file)
Parse given files, create instances of Student class and create instances of Group class
(title for group is name of json-file without extension).
"""

import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, json_file):
        folder = "Test_data/"
        with open(folder +json_file) as f:
            data = json.load(f)
            values = list(data.values())
            return cls(*values)

    @staticmethod
    def serialize_to_json(cls, filename):
        with open(filename, "w") as fw:
            # print(cls.__dict__)
            json.dump(cls.__dict__, fw,indent=None)
    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        pass

    @classmethod
    def create_group_from_file(cld, students_file):

        pass


if __name__ == "__main__":
    ## ========================================
    user1 = Student.from_json("2020-01.json")
    print(user1)
    # Student2 from group2 (50.4): ['C++']

    ## ========================================

    # user1 = Student.from_json("2020-01.json")
    # Student.serialize_to_json(user1, "test_student.json")
    # # print_file("test_student.json")
    # # {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}

    ## ========================================
    #
    # import json
    # folder ="Test_data/"
    # with open(folder + "2020_2.json") as read_file:
    #     user2 = json.load(read_file)
    # print([str(Student(**item)) for item in user2])

    ## ========================================

    g1 = Group.create_group_from_file("2020_2.json")
    g2 = Group.create_group_from_file("2020-01.json")
    Group.serialize_to_json([g1, g2], "g1")
    # print_file("g1")