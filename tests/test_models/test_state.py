#!/usr/bin/python3
""" Defines a class TestState for State module. """
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """Defines tests for State Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.S1 = State()
        cls.S1.name = "ALEX"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.S1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.S1)), result)

    def test_inheritance(self):
        """Test if State is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.S1, State)
        self.assertEqual(type(self.S1), State)
        self.assertEqual(issubclass(self.S1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.S1.id, str)
        self.assertEqual(type(self.S1.id), str)
        self.assertIsInstance(self.S1.created_at, datetime.datetime)
        self.assertIsInstance(self.S1.updated_at, datetime.datetime)
        self.assertIsInstance(self.S1.name, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.S1.save()
        self.assertNotEqual(self.S1.created_at, self.S1.updated_at)

    def test_functions(self):
        """Test if State module is documented.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.S1, 'id'))
        self.assertTrue(hasattr(self.S1, 'created_at'))
        self.assertTrue(hasattr(self.S1, 'updated_at'))
        self.assertTrue(hasattr(self.S1, 'name'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.S1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.S1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.S1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.S1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.S1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        S2 = self.S1.__class__()
        S3 = self.S1.__class__()
        S4 = self.S1.__class__()
        self.assertNotEqual(self.S1.id, S2.id)
        self.assertNotEqual(self.S1.id, S3.id)
        self.assertNotEqual(self.S1.id, S4.id)


if __name__ == '__main__':
    unittest.main()
