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

import json
import pickle
from enum import Enum


# // type your code here
class SerializeManager:
    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type


    def serialize(self, file_name, file_type):
        pass


class FileType(Enum):
    JSON = 1
    def __int__(self):
        pass

def serialize(object, filename, filetype):
    # print(object, filename, filetype)
    # print(SerializeManager(filename, filetype))
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(object)


if __name__ == "__main__":
    print(isinstance(serialize.__globals__['SerializeManager'], object))
    # True
    print(issubclass(FileType, Enum))
    # True

    from os import path

    # print(str(path.exists('1')))
    serialize("String", "1", FileType.JSON)
    print(str(path.exists('1')))
