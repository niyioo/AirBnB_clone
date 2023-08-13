#!/usr/bin/python3
import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()
        self.place.name = "Cozy Cabin"

    def tearDown(self):
        storage.delete(self.place)
        self.place = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "name"))

    def test_save(self):
        original_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(original_updated_at, self.place.updated_at)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
