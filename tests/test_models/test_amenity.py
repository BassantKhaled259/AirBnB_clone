#!/usr/bin/python3
""" module used for testing Amenity.
"""
import datetime
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Defines tests for Amenity Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.A = Amenity()
        cls.A.name = "HaHA"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.A

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.A)), result)

    def test_inheritance(self):
        """Test if Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.A, Amenity)
        self.assertEqual(type(self.A), Amenity)
        self.assertEqual(issubclass(self.A.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.A.name, str)
        self.assertEqual(type(self.A.name), str)
        self.assertIsInstance(self.A.id, str)
        self.assertEqual(type(self.A.id), str)
        self.assertIsInstance(self.A.created_at, datetime.datetime)
        self.assertIsInstance(self.A.updated_at, datetime.datetime)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.A.save()
        self.assertNotEqual(self.A.created_at, self.A.updated_at)

    def test_functions(self):
        """Test if Amenity moudule is documented.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.A, 'name'))
        self.assertTrue(hasattr(self.A, 'id'))
        self.assertTrue(hasattr(self.A, 'created_at'))
        self.assertTrue(hasattr(self.A, 'updated_at'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.A.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.A.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.A.created_at))
        self.assertEqual(module['__class__'],
                         self.A.__class__.__name__)
        self.assertEqual(module['id'], self.A.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        A1 = self.A.__class__()
        A2 = self.A.__class__()
        A3 = self.A.__class__()
        self.assertNotEqual(self.A.id, A1.id)
        self.assertNotEqual(self.A.id, A2.id)
        self.assertNotEqual(self.A.id, A3.id)


if __name__ == '__main__':
    unittest.main()
