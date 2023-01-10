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


class SerializeManager:
    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type

    def __enter__(self):
        mode = self.file_type.mode
        self.file = open(self.file_name, mode)
        return self

    def serialize(self, object):
        modul = self.file_type.modul
        modul.dump(object, self.file)
        # if self.file_type == FileType.JSON:
        #     json.dump(object, self.file)
        # elif self.file_type == FileType.BYTE:
        #     pickle.dump(object, self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class FileType(Enum):
    JSON = (json, "w")
    BYTE = (pickle, "wb")

    def __init__(self, modul, mode):
        self.modul = modul
        self.mode = mode


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


if __name__ == "__main__":
    print(isinstance(serialize.__globals__['SerializeManager'], object))
    # # True
    # print("===================")
    print(issubclass(FileType, Enum))
    # # True
    print("===================")
    from os import path

    print(str(path.exists('1.json')))
    serialize("String", "1.json", FileType.JSON)
    print(str(path.exists('1.json')))
    # True
    # True

    print("===================")
    user_dict = {"name": "Hallo", "id": 2}
    serialize(user_dict, "2.txt", FileType.BYTE)
    with open("2.txt", "rb") as file:
        print(pickle.load(file))
    ## {'name': 'Hallo', 'id': 2}
