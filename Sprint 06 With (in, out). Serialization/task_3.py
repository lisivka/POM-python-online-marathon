"""
In user.json file we have information about users in format
[{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],
in file department.json are information about departments in format:
[{“id”: 1, “name”: “departmentName”}, ...].

Function user_with_department(csv_file, user_json, department_json)
should read from json files information and create csv file in format:
header line - name, department
next lines :  <userName>, <departmentName>
If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.
Create appropriate json-schemas for user and department.
If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception
To validate instances create function validate_json(data, schema)

В файле user.json у нас есть информация о пользователях в формате [{"id": 1, "name": "userName", "department_id": 1}, ...],
в файле Department.json информация об отделах в формате: [{"id": 1, "name": "departmentName"}, ...].

Функция user_with_department(csv_file, user_json, Department_json) должна считывать информацию из файлов json и создавать файл csv в формате:
строка заголовка - название, отдел
следующие строки: <userName>, <departmentName>
Если в файле Department.json нет отдела с ИД_отдела из user.json, мы генерируем исключение «DepartmentName».
Создайте соответствующие json-схемы для пользователя и отдела.
Если схема для пользователя или отдела не соответствует форматам, описанным выше, мы должны сгенерировать исключение InvalidInstanceError.
Для проверки экземпляров создайте функцию validate_json (данные, схема)

"""
import json
import jsonschema
from jsonschema import validate
import csv


def load_json(file):
    folder = ""
    folder = "Test_data/"

    with open(folder + file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


schema_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "user",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        },
        "required": ["id", "name", "department_id"]
    }
}

schema_department = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "departament",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }
}


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)

    except BaseException:
        print(f"InvalidInstanceError {schema['title']} ")


class DepartmentName(Exception):
    def __init__(self, dep_id):
        self.dep_id = dep_id

    def __str__(self):
        return f"DepartmentName={self.dep_id}"


def save_csv(csv_file, data):
    header = ["name", "department"]
    header = ["id", "name", ]
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def user_with_department(csv_file, user_json, department_json):
    user_data = load_json(user_json)
    dep_data = load_json(department_json)
    print(dep_data)

    save_csv(csv_file, dep_data)

    return


if __name__ == "__main__":
    try:
        user_with_department("user_department.csv", "user_without_dep.json", "department.json")
    except DepartmentName as e:
        print(str(e))
