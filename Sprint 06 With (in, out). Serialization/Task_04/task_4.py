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



class StudentEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            data = json.load(f)
            values = list(data.values())
            return cls(*values)

    @staticmethod
    def serialize_to_json(cls, filename):
        with open(filename, "w") as f:
            json.dump(cls.__dict__, f, indent=None)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        return f"{self.title}: {list(map(str, self.students))}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, "w") as f:
            groups = [group.__dict__ for group in list_of_groups]
            # print('========',groups)
            # return json.dump(groups, f, indent=None, default=lambda x: x.__dict__ )
            return json.dump(groups, f, indent=None, cls=StudentEncoder)

    @classmethod
    def create_group_from_file(cls, json_file):
        with open(json_file) as f:
            data = json.load(f)
            if isinstance(data, dict):
                data = [data]
            students = [Student(*list(each.values())) for each in data]
            # title, _ = json_file.split(".")
            title = json_file[:-5]
            return cls(title, students)

    # @classmethod
    # def create_group_from_file(cls, json_file):
    #     with open(json_file) as f:
    #         data = json.load(f)
    #         # title, _ = json_file.split(".")
    #         title = json_file[:-5]
    #         return cls(title, data)


if __name__ == "__main__":
    # ## ========================================
    # user1 = Student.from_json("2020-01.json")
    # print("===", user1)
    # # Student2 from group2 (50.4): ['C++']

    # #
    ## ========================================

    # user1 = Student.from_json("2020-01.json")
    # Student.serialize_to_json(user1, "test_student.json")
    # # print_file("test_student.json")
    # # {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}

    ## ========================================
    #
    # import json

    with open("2020_2.json") as read_file:
        user2 = json.load(read_file)
    print([str(Student(**item)) for item in user2])

    ## ========================================

    g1 = Group.create_group_from_file("2020_2.json")
    print(g1)
    g2 = Group.create_group_from_file("2020-01.json")
    print(g2)
    Group.serialize_to_json([g1, g2], "g1.json")
    # # print_file("g1")
    # # # [{"title": "2020_2",
    # # #   "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]},
    # # #                {"full_name": "Student 2 from second Group", "avg_rank": 70.34,
    # # #                 "courses": ["Ruby", "Python", "Frontend development"]}]},
    # # #  {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]

    g1 = Group.create_group_from_file("2020_2.json")
    print(g1)
    # 2020_2: ["Student 1 from second Group (98): ['Python']",
    #          "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]

    # g2 = Group.create_group_from_file("2020-01.json")
    # print(g2)
    # 2020 - 01: ["Student2 from group2 (50.4): ['C++']"]
