#!/usr/bin/python3
""" Defines a class TestBaseModel for BaseModel module. """
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Defines tests for basemodel Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.BM1 = BaseModel()
        cls.BM1.name = "MY_MODULE"
        cls.BM1.my_number = 89

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.BM1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.BM1)), result)

    def testBM1(self):
        """Test attributes value of a BaseModel instance.
        """
        self.BM1.save()
        my_model_json = self.BM1.to_dict()
        self.assertEqual(self.BM1.name, my_model_json['name'])
        self.assertEqual(self.BM1.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.BM1.id, my_model_json['id'])

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.BM1.name, str)
        self.assertEqual(type(self.BM1.name), str)
        self.assertIsInstance(self.BM1.id, str)
        self.assertEqual(type(self.BM1.id), str)
        self.assertIsInstance(self.BM1.created_at, datetime.datetime)
        self.assertIsInstance(self.BM1.updated_at, datetime.datetime)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.BM1.save()
        self.assertNotEqual(self.BM1.created_at,
                     self.BM1.updated_at)
        
    def test_functions(self):
        """Test if BaseModel moudule is documented.
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.BM1, 'name'))
        self.assertTrue(hasattr(self.BM1, 'id'))
        self.assertTrue(hasattr(self.BM1, 'created_at'))
        self.assertTrue(hasattr(self.BM1, 'updated_at'))

    def test_set_attributes(self):
        """Test set attributes of BaseModel.
        """
        self.assertEqual(self.BM1.name, "MY_MODULE")
        self.assertEqual(self.BM1.my_number, 89)

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.BM1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.BM1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.BM1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.BM1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.BM1.id)

    def test_unique_id(self):
        """test if the id is unique.
        """
        base2 = self.BM1.__class__()
        base3 = self.BM1.__class__()
        base4 = self.BM1.__class__()
        self.assertNotEqual(self.BM1.id, base2.id)
        self.assertNotEqual(self.BM1.id, base3.id)
        self.assertNotEqual(self.BM1.id, base4.id)

    def test__str__(self):
        """testing __str__ representation
        """
        self = self.BaseModel()
        utput = f"[BaseModel] ({self.id}) {self.__dict__}"
        self.assertEqual(self.__str__(), utput)

        """
        string = str(self.BaseModel1)
        id_test = "[BaseModel] ({})".format(self.BaseModel1.id)
        boolean = id_test in string
        self.assertEqual(True, boolean)
        boolean = "updated_at" in string
        self.assertEqual(True, boolean)
        boolean = "created_at" in string
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in string
        self.assertEqual(True, boolean)
        """

if __name__ == '__main__':
    unittest.main()