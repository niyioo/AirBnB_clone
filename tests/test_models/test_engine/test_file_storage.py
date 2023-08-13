#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        self.storage.delete(self.base_model)
        self.storage = None
        self.base_model = None

    def test_all(self):
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(self.base_model, all_objs.values())

    def test_new(self):
        new_base_model = BaseModel()
        new_base_model.name = "New Model"
        self.storage.new(new_base_model)
        all_objs = self.storage.all()
        self.assertIn(new_base_model, all_objs.values())

    def test_save(self):
        self.base_model.save()
        all_objs = self.storage.all()
        self.assertIn(self.base_model, all_objs.values())

    def test_reload(self):
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(self.base_model, all_objs.values())

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
