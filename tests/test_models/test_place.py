#!/usr/bin/python3
"""
Unit tests for Place class
"""

import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """
    Test suite for Place class
    """

    def setUp(self):
        """Set up test instance"""
        self.place = Place()
        self.place.name = "Cozy Cabin"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.place)
        self.place = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.place, "name"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(original_updated_at, self.place.updated_at)

    def test_name_type(self):
        """Test if 'name' attribute is of type str"""
        self.assertIsInstance(self.place.name, str)

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_number_of_rooms(self):
        """Test the number_of_rooms attribute"""
        self.place.number_of_rooms = 3
        self.assertEqual(self.place.number_of_rooms, 3)

    def test_number_of_bathrooms(self):
        """Test the number_of_bathrooms attribute"""
        self.place.number_of_bathrooms = 2
        self.assertEqual(self.place.number_of_bathrooms, 2)


if __name__ == "__main__":
    unittest.main()
