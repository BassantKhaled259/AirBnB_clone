#!/usr/bin/python3
""" Defines a class TestAmenity for Amenity module. """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime


class TestAmenity(unittest.TestCase):
    """Defines tests for Amenity Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.A1 = Amenity()
        cls.A1.name = "pH"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.A1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.all_models.Amenity'>"
        self.assertEqual(str(type(self.A1)), result)

    def test_inheritance(self):
        """Test if Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.A1, Amenity)
        self.assertEqual(type(self.A1), Amenity)
        self.assertEqual(issubclass(self.A1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.A1.name, str)
        self.assertEqual(type(self.A1.name), str)
        self.assertIsInstance(self.A1.id, str)
        self.assertEqual(type(self.A1.id), str)
        self.assertIsInstance(self.A1.created_at, datetime.datetime)
        self.assertIsInstance(self.A1.updated_at, datetime.datetime)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.A1.save()
        self.assertNotEqual(self.A1.created_at, self.A1.updated_at)

    def test_functions(self):
        """Test if Amenity moudule is documented.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.A1, 'name'))
        self.assertTrue(hasattr(self.A1, 'id'))
        self.assertTrue(hasattr(self.A1, 'created_at'))
        self.assertTrue(hasattr(self.A1, 'updated_at'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.A1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.A1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.A1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.A1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.A1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        A2 = self.A1.__class__()
        A3 = self.A1.__class__()
        A4 = self.A1.__class__()
        self.assertNotEqual(self.A1.id, A2.id)
        self.assertNotEqual(self.A1.id, A3.id)
        self.assertNotEqual(self.A1.id, A4.id)


if __name__ == '__main__':
    unittest.main()
