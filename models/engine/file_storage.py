#!/usr/bin/python3
"""This documents FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage class implementation."""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self) -> None:
        """Constructs an instance of FileStorage."""
        pass

    def all(self) -> dict:
        """This returns a dictionary of all objects."""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in `__objects` the `obj` with key `<obj class name>.id`"""
        self.__objects[
            f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self) -> None:
        """Serialize `__objects` to JSON file specified in `__file_path`."""
        with open(__class__.__file_path, 'w') as json_file:
            tmp_storage = {}
            for key, value in self.__objects.items():
                tmp_storage[key] = value.to_dict()
            json.dump(tmp_storage, json_file)

    def reload(self) -> None:
        """Deserialize JSON file specified in `__file_path` to `__objects`"""
        try:
            with open(self.__file_path) as json_file:
                for key, value in json.load(json_file).items():
                    tmp_obj = eval(f'{value["__class__"]}(**{value})')
                    self.__objects[key] = tmp_obj
        except Exception:
            pass

    def delete(cls, key):
        """This deletes key from __objects."""
        __class__.__objects.pop(key)
