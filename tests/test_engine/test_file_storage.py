#!/usr/bin/python3
""" Defines a class TestFileStorage for FileStorage module. """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os

class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.model1 = BaseModel()
        cls.file1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.model1
        del cls.file1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.file1)), result)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.file1, FileStorage)
        self.assertEqual(type(self.file1), FileStorage)

    def test_functions(self):
        """Test if FileStorage module is documented.
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """Test if save method is working correctly."""
        
        self.file1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Tests if reload method is working correctly.
        """
        # convert_to_dict = {key: obj.to_dict() for key, obj
        # in self.__objects.items()}
        
        self.model1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dictionary = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dictionary, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dictionary[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
