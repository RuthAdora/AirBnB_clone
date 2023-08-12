import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test the __init__ method
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        # Test the __str__ method
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn(obj.__class__.__name__, obj_str)
        self.assertIn(obj.id, obj_str)
        self.assertIn(str(obj.__dict__), obj_str)

    def test_save(self):
        # Test the save method
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if __name__ == '__main__':
    unittest.main()
