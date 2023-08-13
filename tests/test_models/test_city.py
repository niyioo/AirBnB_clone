#!/usr/bin/python3
import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()
        self.city.name = "New York"

    def tearDown(self):
        storage.delete(self.city)
        self.city = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "name"))

    def test_save(self):
        original_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
