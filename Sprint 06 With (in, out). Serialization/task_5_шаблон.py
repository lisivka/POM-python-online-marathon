'''
Create context manager class SerializeManager with attributes filename
and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type.
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, filetype).
This function use SerializeManager and should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2"
and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"
'''
# https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
# https://docs-python.ru/standart-library/modul-enum-perechislenija-python/
# https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/context_managers

import json
import pickle
from enum import Enum


# // type your code here
class SerializeManager:
    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type
        # self.file = None

    def __enter__(self):
        print("__enter__")
        self.file = open(self.file_name, 'w')
        return self

    def serialize(self, object):
        print("_serialize_")
        json.dump(object, self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.file.close()


class FileType(Enum):
    JSON = "json"


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


if __name__ == "__main__":
    # print(isinstance(serialize.__globals__['SerializeManager'], object))
    # # True
    # print(issubclass(FileType, Enum))
    # # True

    from os import path

    # print(str(path.exists('1')))
    serialize("String", "1.json", FileType.JSON)
    print(str(path.exists('1')))
