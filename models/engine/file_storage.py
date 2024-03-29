#!/usr/bin/python3
# Modify our file storage

"""
@authors: Clevers Rungene
          Lawrence Ongaki
    File Storage Module
"""
""" Convert the dictionary representation to a JSON string """i
from models.base_model import BaseModel
import os
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serialization/deserialization objects
    into and from files.
    Attributes:
        __file_path(string) - path to the JSON file
        __objects (dictionary) - empty but will store all
        objects by <class name>.id
         (ex: to store a BaseModel object with id=12121212,
         the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """Init method for file storage class"""
        pass

    def all(self):
        """public instance method
        Return:
             returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Attributes:
            obj(Python object): The object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
