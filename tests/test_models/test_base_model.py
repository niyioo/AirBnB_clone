#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"

    def tearDown(self):
        storage.delete(self.base_model)
        self.base_model = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "name"))

    def test_save(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], "BaseModel")
        self.assertEqual(base_model_dict['name'], "Test Model")

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
