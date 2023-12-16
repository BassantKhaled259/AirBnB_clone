#!/usr/bin/python3
""" module used for testing City.
"""

import datetime
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Defines tests for City Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.c = City()
        cls.c.name = "Alex"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.c

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.c)), result)

    def test_inheritance(self):
        """Test if Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.c, City)
        self.assertEqual(type(self.c), City)
        self.assertEqual(issubclass(self.c.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.c.name, str)
        self.assertEqual(type(self.c.name), str)
        self.assertIsInstance(self.c.id, str)
        self.assertEqual(type(self.c.id), str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)
        self.assertIsInstance(self.c.state_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.c.save()
        self.assertNotEqual(self.c.created_at, self.c.updated_at)

    def test_functions(self):
        """Test if City moudule is documented.
        """
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))
        self.assertTrue(hasattr(self.c, 'state_id'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.c.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.c.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.c.created_at))
        self.assertEqual(module['__class__'],
                         self.c.__class__.__name__)
        self.assertEqual(module['id'], self.c.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        c1 = self.c.__class__()
        c2 = self.c.__class__()
        c3 = self.c.__class__()
        self.assertNotEqual(self.c.id, c1.id)
        self.assertNotEqual(self.c.id, c2.id)
        self.assertNotEqual(self.c.id, c3.id)


if __name__ == '__main__':
        unittest.main()
