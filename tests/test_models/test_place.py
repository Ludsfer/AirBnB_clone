#!/usr/bin/python3
"""Test suite for the Place class of the models.place module"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        self.place = Place()
        self.attr_list = ["city_id", "user_id", "name",
                "description", "number_rooms",
                "number_bathrooms", "max_guest",
                "price_by_night", "latitude",
                "longitude", "amenity_ids"]

    def test_place_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))
