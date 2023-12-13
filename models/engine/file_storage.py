#!/usr/bin/python3
"""Storage module for storing the date as JSON format
"""

from models.all_models import our_models
import json
import os

class FileStorage():
    """Class sued for serialization and deserialization 
    Attrs:
        file_path: path to JSON file
        objects: dictionary to store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates new instances of class.
        """
        pass

    def all(self):
        """Returns the dictionary objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets in objects attribute the obj with className.<id> as key.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """method used for converting python object into JSON string
        """
        # dictionary = {key: obj.to_dict()
        # for key, obj in FileStorage.__objects.items()}.

        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, mode = 'w', encoding="utf-8") as path:
            json.dump(dictionary, path)

    def reload(self):
        """method used for converting JSON string into python object.
        """
        try:
            with open(self.__file_path, mode = 'r', encoding='utf-8') as path:
                data = path.read()
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = our_models[class_name](**value)
                    self.__objects[key] = obj
                    # self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Deletes obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False