#!/usr/bin/python3
""" Defines a class TestPlace for Place module. """
import unittest
from models.place import Place
from models.base_model import BaseModel
from models.all_models import all_models
import datetime


class TestPlace(unittest.TestCase):
    """Defines tests for Place Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.P1 = Place()
        cls.P1.name = "ALEX"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.P1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.P1)), result)

    def test_inheritance(self):
        """Test if Place is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.P1, Place)
        self.assertEqual(type(self.P1), Place)
        self.assertEqual(issubclass(self.P1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.P1.name, str)
        self.assertEqual(type(self.P1.name), str)
        self.assertIsInstance(self.P1.id, str)
        self.assertEqual(type(self.P1.id), str)
        self.assertIsInstance(self.P1.created_at, datetime.datetime)
        self.assertIsInstance(self.P1.updated_at, datetime.datetime)
        self.assertIsInstance(self.P1.amenity_ids, list)
        self.assertIsInstance(self.P1.longitude, float)
        self.assertIsInstance(self.P1.latitude, float)
        self.assertIsInstance(self.P1.price_by_night, int)
        self.assertIsInstance(self.P1.max_guest, int)
        self.assertIsInstance(self.P1.description, str)
        self.assertIsInstance(self.P1.number_rooms, int)
        self.assertIsInstance(self.P1.number_bathrooms, int)
        self.assertIsInstance(self.P1.city_id, str)
        self.assertIsInstance(self.P1.user_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.P1.save()
        self.assertNotEqual(self.P1.created_at, self.P1.updated_at)

    def test_functions(self):
        """Test if Place module is documented.
        """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.P1, 'name'))
        self.assertTrue(hasattr(self.P1, 'id'))
        self.assertTrue(hasattr(self.P1, 'created_at'))
        self.assertTrue(hasattr(self.P1, 'updated_at'))
        self.assertTrue(hasattr(self.P1, 'city_id'))
        self.assertTrue(hasattr(self.P1, 'user_id'))
        self.assertTrue(hasattr(self.P1, 'description'))
        self.assertTrue(hasattr(self.P1, 'number_rooms'))
        self.assertTrue(hasattr(self.P1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.P1, 'max_guest'))
        self.assertTrue(hasattr(self.P1, 'price_by_night'))
        self.assertTrue(hasattr(self.P1, 'latitude'))
        self.assertTrue(hasattr(self.P1, 'longitude'))
        self.assertTrue(hasattr(self.P1, 'amenity_ids'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.P1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.P1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.P1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.P1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.P1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        P2 = self.P1.__class__()
        P3 = self.P1.__class__()
        P4 = self.P1.__class__()
        self.assertNotEqual(self.P1.id, P2.id)
        self.assertNotEqual(self.P1.id, P3.id)
        self.assertNotEqual(self.P1.id, P4.id)


if __name__ == '__main__':
    unittest.main()
