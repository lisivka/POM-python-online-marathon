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
"""