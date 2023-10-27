#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage definition."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj_class_name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_data, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects."""
        try:
            with open(self.__file_path) as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    cls = None
                    if class_name in globals():
                        cls = globals()[class_name]
                        del obj_dict['__class__']
                    if cls:
                        obj = cls(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            return
