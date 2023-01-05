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
    "title": "department",
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


class InvalidInstanceError(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Error in {self.name} schema'


class DepartmentName(Exception):
    def __init__(self, dep_id):
        self.dep_id = dep_id

    def __str__(self):
        return f"Department with id {self.dep_id} doesn't exists"


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)

    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(f"{schema['title']}")


def save_csv(csv_file, data):
    header = ["name", "department"]

    with open(csv_file, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def get_user_departament(data: list, dep_id: int):
    dep_name = None
    for dep in data:
        if dep['id'] == dep_id:
            dep_name = dep["name"]
    return dep_name


def user_with_department(csv_file, user_json, department_json):
    user_data = load_json(user_json)
    dep_data = load_json(department_json)
    new_dict = []
    validate_json(user_data, schema_user)
    validate_json(dep_data, schema_department)

    for user in user_data:
        dep_name = get_user_departament(dep_data, user["department_id"])
        if dep_name is None:
            raise DepartmentName(user["department_id"])
        new_dict.append({"name": user["name"], "department": dep_name})

    save_csv(csv_file, new_dict)

    return


if __name__ == "__main__":

    ## ========================================
    try:
        user_with_department("user_department.csv", "user_without_dep.json", "department.json")
    except DepartmentName as e:
        print(str(e))

    ## ========================================
    user_with_department("user_department.csv", "user.json", "department.json")
    ## print_file("user_department.csv")

    ## ========================================
    try:
        user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
    except InvalidInstanceError as e:
        print(str(e))

    ## ========================================

    try:
        user_with_department("user_department.csv", "user.json", "department_without_id.json")
    except InvalidInstanceError as e:
        print(str(e))
