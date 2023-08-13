#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity
from models import storage
import sys


sys.path.append("..")

class TestAmenity(unittest.TestCase):
    """Test suite for Amenity class"""

    def setUp(self):
        """Set up test instance"""
        self.amenity = Amenity()
        self.amenity.name = "Free Wi-Fi"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.amenity)
        self.amenity = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Test the to_dict() method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Free Wi-Fi')

    def test_from_dict(self):
        """Test the from_dict() method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.id, self.amenity.id)
        self.assertEqual(new_amenity.name, self.amenity.name)
        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()
