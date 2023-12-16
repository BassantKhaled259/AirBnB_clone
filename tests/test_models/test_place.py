#!/usr/bin/python3
"""module used for testing Place.
"""
import datetime
import unittest
from models.place import Place
from models.base_model import BaseModel



class TestPlace(unittest.TestCase):
    """Defines tests for Place Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.p = Place()
        cls.p.name = "Alex"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.p

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.p)), result)

    def test_inheritance(self):
        """Test if Place is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.p, Place)
        self.assertEqual(type(self.p), Place)
        self.assertEqual(issubclass(self.p.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.p.name, str)
        self.assertEqual(type(self.p.name), str)
        self.assertIsInstance(self.p.id, str)
        self.assertEqual(type(self.p.id), str)
        self.assertIsInstance(self.p.created_at, datetime.datetime)
        self.assertIsInstance(self.p.updated_at, datetime.datetime)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.p.save()
        self.assertNotEqual(self.p.created_at, self.p.updated_at)

    def test_functions(self):
        """Test if Place module is documented.
        """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.p.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.p.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.p.created_at))
        self.assertEqual(module['__class__'],
                         self.p.__class__.__name__)
        self.assertEqual(module['id'], self.p.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        p1 = self.p.__class__()
        p2 = self.p.__class__()
        p3 = self.p.__class__()
        self.assertNotEqual(self.p.id, p1.id)
        self.assertNotEqual(self.p.id, p2.id)
        self.assertNotEqual(self.p.id, p3.id)


if __name__ == '__main__':
    unittest.main()
