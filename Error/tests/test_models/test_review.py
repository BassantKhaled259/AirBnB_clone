#!/usr/bin/python3
""" Defines a class TestReview for Review module. """
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
        cls.R1 = Review()
        cls.R1.name = "ALEX"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.R1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.R1)), result)

    def test_inheritance(self):
        """Test if Review is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.R1, Review)
        self.assertEqual(type(self.R1), Review)
        self.assertEqual(issubclass(self.R1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.R1.id, str)
        self.assertEqual(type(self.R1.id), str)
        self.assertIsInstance(self.R1.created_at, datetime.datetime)
        self.assertIsInstance(self.R1.updated_at, datetime.datetime)
        self.assertIsInstance(self.R1.text, str)
        self.assertIsInstance(self.R1.place_id, str)
        self.assertIsInstance(self.R1.user_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.R1.save()
        self.assertNotEqual(self.R1.created_at, self.R1.updated_at)

    def test_functions(self):
        """Test if Review module is documented.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.R1, 'id'))
        self.assertTrue(hasattr(self.R1, 'created_at'))
        self.assertTrue(hasattr(self.R1, 'updated_at'))
        self.assertTrue(hasattr(self.R1, 'user_id'))
        self.assertTrue(hasattr(self.R1, 'text'))
        self.assertTrue(hasattr(self.R1, 'place_id'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.R1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.R1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.R1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.R1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.R1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        R2 = self.R1.__class__()
        R3 = self.R1.__class__()
        R4 = self.R1.__class__()
        self.assertNotEqual(self.R1.id, R2.id)
        self.assertNotEqual(self.R1.id, R3.id)
        self.assertNotEqual(self.R1.id, R4.id)


if __name__ == '__main__':
    unittest.main()
