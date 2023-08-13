#!/usr/bin/python3
"""
Unit tests for City class
"""

import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """
    Test suite for City class
    """

    def setUp(self):
        """Set up test instance"""
        self.city = City()
        self.city.name = "New York"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.city)
        self.city = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.city, "name"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    def test_name_type(self):
        """Test if 'name' attribute is of type str"""
        self.assertIsInstance(self.city.name, str)

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == "__main__":
    unittest.main()
