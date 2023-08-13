#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up testing environment"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        """Tear down testing environment"""
        self.storage.delete(self.base_model)
        self.storage = None
        self.base_model = None

    def test_all(self):
        """Test the all() method of FileStorage"""
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(self.base_model, all_objs.values())

    def test_new(self):
        """Test the new() method of FileStorage"""
        new_base_model = BaseModel()
        new_base_model.name = "New Model"
        self.storage.new(new_base_model)
        all_objs = self.storage.all()
        self.assertIn(new_base_model, all_objs.values())

    def test_save(self):
        """Test the save() method of FileStorage"""
        self.base_model.save()
        all_objs = self.storage.all()
        self.assertIn(self.base_model, all_objs.values())

    def test_reload(self):
        """Test the reload() method of FileStorage"""
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(self.base_model, all_objs.values())

    def test_delete(self):
        """Test the delete() method of FileStorage"""
        self.storage.delete(self.base_model)
        all_objs = self.storage.all()
        self.assertNotIn(self.base_model, all_objs.values())

    def test_count(self):
        """Test the count() method of FileStorage"""
        count = self.storage.count()
        self.assertEqual(count, 1)

    def test_get(self):
        """Test the get() method of FileStorage"""
        retrieved_obj = self.storage.get(BaseModel, self.base_model.id)
        self.assertEqual(retrieved_obj, self.base_model)

    def test_get_nonexistent(self):
        """Test the get() method with a nonexistent object"""
        retrieved_obj = self.storage.get(BaseModel, "nonexistent_id")
        self.assertIsNone(retrieved_obj)


if __name__ == "__main__":
    unittest.main()
