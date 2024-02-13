#!/usr/bin/python3
"""
    Defines FileStorage class module
"""
import json
import models
import os
from console import new_classes


class FileStorage:
    """
    Class for serializing and deserializing JSON files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects 

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_key = str(obj.__class__.__name__) + "." + str(obj.id)
        obj_value = obj
        FileStorage.__objects[obj_key] = obj_value

    def save(self):
        """
        Serializes the objects into JSON file
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """
        Deserializes a JSON file into __objects
        """
        try:
            if self.__file_path and os.path.getsize(self.__file_path) != 0:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                    FileStorage.__objects = json.load(fd)
                for key, val in FileStorage.__objects.items():
                    class_name = val["__class__"]
                    class_name = new_classes[class_name]
                    FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

