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
        cls.u = User()
        cls.u.name = "Boss"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.u

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.u)), result)

    def test_inheritance(self):
        """Test if User is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.u, User)
        self.assertEqual(type(self.u), User)
        self.assertEqual(issubclass(self.u.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.u.id, str)
        self.assertEqual(type(self.u.id), str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.u.save()
        self.assertNotEqual(self.u.created_at, self.u.updated_at)

    def test_functions(self):
        """Test if User module is documented.
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.u.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.u.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.u.created_at))
        self.assertEqual(module['__class__'],
                         self.u.__class__.__name__)
        self.assertEqual(module['id'], self.u.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        u1 = self.u.__class__()
        u2 = self.u.__class__()
        u3 = self.u.__class__()
        self.assertNotEqual(self.u.id, u1.id)
        self.assertNotEqual(self.u.id, u2.id)
        self.assertNotEqual(self.u.id, u3.id)


if __name__ == '__main__':
    unittest.main()
