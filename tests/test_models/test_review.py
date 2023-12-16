#!/usr/bin/python3
"""module used for testing Review.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import datetime


class TestReview(unittest.TestCase):
    """Defines tests for Review Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.r = Review()
        cls.r.name = "Alex"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.r

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), result)

    def test_inheritance(self):
        """Test if Review is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.r, Review)
        self.assertEqual(type(self.r), Review)
        self.assertEqual(issubclass(self.r.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.r.id, str)
        self.assertEqual(type(self.r.id), str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.r.save()
        self.assertNotEqual(self.r.created_at, self.r.updated_at)

    def test_functions(self):
        """Test if Review module is documented.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'place_id'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.r.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.r.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.r.created_at))
        self.assertEqual(module['__class__'],
                         self.r.__class__.__name__)
        self.assertEqual(module['id'], self.r.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        r1 = self.r.__class__()
        r2 = self.r.__class__()
        r3 = self.r.__class__()
        self.assertNotEqual(self.r.id, r1.id)
        self.assertNotEqual(self.r.id, r2.id)
        self.assertNotEqual(self.r.id, r3.id)


if __name__ == '__main__':
    unittest.main()
