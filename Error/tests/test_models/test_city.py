#!/usr/bin/python3
""" Defines a class TestBaseModel for BaseModel module. """
import unittest
from models.all_models import City
from models.base_model import BaseModel
import datetime


class TestCity(unittest.TestCase):
    """Defines tests for City Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.c1 = BaseModel()
        cls.c1.name = "MY_CITY"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.c1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.all_models.City'>"
        self.assertEqual(str(type(self.c1)), result)

    def test_inheritance(self):
        """Test if City is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.c1, City)
        self.assertEqual(type(self.c1city1), City)
        self.assertEqual(issubclass(self.cic1ty1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.c1.name, str)
        self.assertEqual(type(self.c1.name), str)
        self.assertIsInstance(self.c1.id, str)
        self.assertEqual(type(self.c1.id), str)
        self.assertIsInstance(self.c1.created_at, datetime.datetime)
        self.assertIsInstance(self.c1.updated_at, datetime.datetime)
        self.assertIsInstance(self.c1.state_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_functions(self):
        """Test if City moudule is documented.
        """
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.c1, 'name'))
        self.assertTrue(hasattr(self.c1, 'id'))
        self.assertTrue(hasattr(self.c1, 'created_at'))
        self.assertTrue(hasattr(self.c1, 'updated_at'))
        self.assertTrue(hasattr(self.c1, 'state_id'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.c1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.c1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.c1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.c1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.c1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        c2= self.c1.__class__()
        c3 = self.c1.__class__()
        c4 = self.c1.__class__()
        self.assertNotEqual(self.c1.id, c2.id)
        self.assertNotEqual(self.c1.id, c3.id)
        self.assertNotEqual(self.c1.id, c4.id)


if __name__ == '__main__':
    unittest.main()
