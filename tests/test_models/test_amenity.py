#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Free Wi-Fi"

    def tearDown(self):
        storage.delete(self.amenity)
        self.amenity = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_save(self):
        original_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
