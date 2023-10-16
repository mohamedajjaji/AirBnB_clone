#!/usr/bin/python3
""" Defines unittests for models/base_model.py

    Unittest classes:
        TestBaseModel_instantiation
        TestBaseModel_save
        TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestMyModel(unittest.TestCase):
    """ Unittests for MyModel class """

    def test_my_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key, type(my_model_json[key]),
                my_model_json[key]
                ))


if __name__ == "__main__":
    unittest.main()
