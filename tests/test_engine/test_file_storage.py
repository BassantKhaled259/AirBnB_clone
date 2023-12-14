#!/usr/bin/python3
""" Defines a class TestFileStorage for FileStorage module. """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.all_models import all_models
import os


class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.B_M1 = BaseModel()
        cls.FP1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.B_M1
        del cls.FP1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.FP1)), result)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.FP1, FileStorage)
        self.assertEqual(type(self.FP1), FileStorage)

    def test_functions(self):
        """Test if FileStorage module is documented.
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """Test if save method is working correctly.
        """
        self.FP1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Tests if reload method is working correctly.
        """
        self.B_M1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        CONTENT = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(CONTENT, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(CONTENT[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
