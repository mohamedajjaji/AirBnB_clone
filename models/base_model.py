#!/usr/bin/python3
""" Module: base_model.py """
import uuid
from datetime import datetime


class BaseModel():
    """ Base class which defines all common attributes/methods
    for other classes """

    def __init__(self):
        """ Instantiate an object with its attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of the instance """
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance """
        obj_dict = {self.__dict__}
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
