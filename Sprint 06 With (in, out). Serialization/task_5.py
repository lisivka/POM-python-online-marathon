'''
Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type.
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, filetype).
This function use SerializeManager and should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"
'''

import json
import pickle
from enum import Enum

# // type your code here

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


# print(isinstance(serialize.__globals__['SerializeManager'], object))
# True