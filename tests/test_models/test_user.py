#!/usr/bin/python3
""" Defines a class TestUser for User module. """
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """Defines tests for User Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.USR1 = User()
        cls.USR1.name = "BOSS"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.USR1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.USR1)), result)

    def test_inheritance(self):
        """Test if User is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.USR1, User)
        self.assertEqual(type(self.USR1), User)
        self.assertEqual(issubclass(self.USR1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.USR1.id, str)
        self.assertEqual(type(self.USR1.id), str)
        self.assertIsInstance(self.USR1.created_at, datetime.datetime)
        self.assertIsInstance(self.USR1.updated_at, datetime.datetime)
        self.assertIsInstance(self.USR1.first_name, str)
        self.assertIsInstance(self.USR1.last_name, str)
        self.assertIsInstance(self.USR1.email, str)
        self.assertIsInstance(self.USR1.password, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.USR1.save()
        self.assertNotEqual(self.USR1.created_at, self.USR1.updated_at)

    def test_functions(self):
        """Test if User module is documented.
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.USR1, 'id'))
        self.assertTrue(hasattr(self.USR1, 'created_at'))
        self.assertTrue(hasattr(self.USR1, 'updated_at'))
        self.assertTrue(hasattr(self.USR1, 'first_name'))
        self.assertTrue(hasattr(self.USR1, 'last_name'))
        self.assertTrue(hasattr(self.USR1, 'email'))
        self.assertTrue(hasattr(self.USR1, 'password'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.USR1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.USR1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.USR1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.USR1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.USR1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        USR2 = self.USR1.__class__()
        USR3 = self.USR1.__class__()
        USR4 = self.USR1.__class__()
        self.assertNotEqual(self.USR1.id, USR2.id)
        self.assertNotEqual(self.USR1.id, USR3.id)
        self.assertNotEqual(self.USR1.id, USR4.id)


if __name__ == '__main__':
    unittest.main()
