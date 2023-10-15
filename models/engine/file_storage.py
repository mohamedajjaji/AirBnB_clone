#!/usr/bin/python3
""" Defines the FileStorage class """
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City


class FileStorage():
    """ Represent an abstracted storage engine """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """instantiation method for class
        """
        pass

    def all(self):
        """ Return the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id """
        try:
            obj_n = obj.to_dict()
        except AttributeError:
            raise TypeError('object passed to filestorage has no to_dict()')
        key = obj_n['__class__'] + '.' + str(obj_n['id'])
        self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as myFile:
            json.dump(objdict, myFile)

    def reload(self):
        """ Deserialize the JSON file __file_path to __objects,
        if it exists """
        try:
            with open(FileStorage.__file_path) as myFile:
                objdict = json.load(myFile)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
