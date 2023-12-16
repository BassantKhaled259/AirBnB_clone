#!/usr/bin/python3
"""module used for testing State.
"""
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
        cls.s = State()
        cls.s.name = "Alex"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.s

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), result)

    def test_inheritance(self):
        """Test if State is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.s, State)
        self.assertEqual(type(self.s), State)
        self.assertEqual(issubclass(self.s.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.s.id, str)
        self.assertEqual(type(self.s.id), str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)
        self.assertIsInstance(self.s.name, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.s.save()
        self.assertNotEqual(self.s.created_at, self.s.updated_at)

    def test_functions(self):
        """Test if State module is documented.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))
        self.assertTrue(hasattr(self.s, 'name'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module= self.s.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.s.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.s.created_at))
        self.assertEqual(module['__class__'],
                         self.s.__class__.__name__)
        self.assertEqual(module['id'], self.s.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        s1 = self.s.__class__()
        s2 = self.s.__class__()
        s3 = self.s.__class__()
        self.assertNotEqual(self.s.id, s1.id)
        self.assertNotEqual(self.s.id, s2.id)
        self.assertNotEqual(self.s.id, s3.id)


if __name__ == '__main__':
    unittest.main()
