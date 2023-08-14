#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

import unittest
import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel class"""

    def setUp(self):
        """Set up test instance"""
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"  # Set the name attribute
        self.storage = FileStorage()
        self.storage.new(self.base_model)

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.base_model)
        self.base_model = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.base_model, "name"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], "BaseModel")
        self.assertEqual(base_model_dict['name'], "Test Model")

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_id_generation(self):
        """Test the uniqueness of generated IDs"""
        other_instance = BaseModel()
        self.assertNotEqual(self.base_model.id, other_instance.id)

    def test_created_at(self):
        """Test if created_at is properly set"""
        self.assertTrue(hasattr(self.base_model, "created_at"))

    def test_updated_at_type(self):
        """Test if updated_at is of datetime type"""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation_no_attrs(self):
        """Test __str__ representation with no attributes"""
        empty_base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            empty_base_model.id, empty_base_model.__dict__)
        self.assertEqual(str(empty_base_model), expected_str)

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with kwargs"""
        data = {"name": "Test Model"}
        instance = BaseModel(**data)
        self.assertEqual(instance.name, data["name"])

    def test_updated_at_after_save(self):
        """Test if updated_at changes after calling save()"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_type(self):
        """Test the type of the returned dict from to_dict()"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

    def test_to_dict_created_at(self):
        """Test if 'created_at' exists in the to_dict() output"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn("created_at", base_model_dict)

    def test_to_dict_updated_at(self):
        """Test if 'updated_at' exists in the to_dict() output"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn("updated_at", base_model_dict)

    def test_to_dict_id(self):
        """Test if 'id' exists in the to_dict() output"""
        base_model_dict = self.base_model.to_dict()
        self.assertIn("id", base_model_dict)

    def test_from_dict(self):
        """Test creating an instance from a dictionary"""
        base_model_dict = self.base_model.to_dict()
        new_instance = BaseModel(**base_model_dict)
        self.assertEqual(self.base_model.id, new_instance.id)
        self.assertEqual(self.base_model.created_at, new_instance.created_at)


if __name__ == "__main__":
    unittest.main()
