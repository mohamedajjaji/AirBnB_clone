#!/usr/bin/python3
""" Module: base_model.py """
from uuid import uuid4
import models
from datetime import datetime


class BaseModel():
    """ Base class which defines all common attributes/methods
    for other classes """

    def __init__(self, *args, **kwargs):
        """ Instantiate an object with its attributes """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, fmt)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def __str__(self):
        """ Returns the string representation of the instance """
        s = self.__class__.__name__
        return "[{}] ({}) {}".format(s, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
