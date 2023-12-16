#!/usr/bin/python3
""" module used for testing basemodel
"""
import datetime
import unittest
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """Defines tests for basemodel Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.Model = BaseModel()
        cls.Model.name = "My_first_try"
        cls.Model.my_number = 89

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.Model

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.Model)), result)

    def testBaseModel1(self):
        """Test attributes value of a BaseModel instance.
        """
        self.Model.save()
        module = self.Model.to_dict()

        self.assertEqual(self.Model.name, module['name'])
        self.assertEqual(self.Model.my_number, module['my_number'])
        self.assertEqual('BaseModel', module['__class__'])
        self.assertEqual(self.Model.id, module['id'])

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.Model.name, str)
        self.assertEqual(type(self.Model.name), str)
        
        self.assertIsInstance(self.Model.id, str)
        self.assertEqual(type(self.Model.id), str)
        
        self.assertIsInstance(self.Model.created_at, datetime.datetime)
        self.assertIsInstance(self.Model.updated_at, datetime.datetime)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.Model.save()
        self.assertNotEqual(self.Model.created_at,
                            self.Model.updated_at)

    def test_functions(self):
        """Test if BaseModel moudule is documented.
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.Model, 'name'))
        self.assertTrue(hasattr(self.Model, 'id'))
        self.assertTrue(hasattr(self.Model, 'created_at'))
        self.assertTrue(hasattr(self.Model, 'updated_at'))

    def test_set_attributes(self):
        """Test set attributes of BaseModel.
        """
        self.assertEqual(self.Model.name, "My_first_try")
        self.assertEqual(self.Model.my_number, 89)

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        module = self.Model.to_dict()
        self.assertEqual(str, type(module['created_at']))
        self.assertEqual(module['created_at'],
                         self.Model.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.Model.created_at))
        self.assertEqual(module['__class__'],
                         self.Model.__class__.__name__)
        self.assertEqual(module['id'], self.Model.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        Model1 = self.Model.__class__()
        model2 = self.Model.__class__()
        model3 = self.Model.__class__()
        self.assertNotEqual(self.Model.id, Model1.id)
        self.assertNotEqual(self.Model.id, model2.id)
        self.assertNotEqual(self.Model.id, model3.id)

    def test__str__(self):
        """Test if __str__ method returns expected string.
        """
        # boolen: true or false method.
        string = str(self.Model)
        id_test = "[BaseModel] ({})".format(self.Model.id)
        boolean = id_test in string
        self.assertEqual(True, boolean)
        boolean = "updated_at" in string
        self.assertEqual(True, boolean)
        boolean = "created_at" in string
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in string
        self.assertEqual(True, boolean)


if __name__ == '__main__':
    unittest.main()
