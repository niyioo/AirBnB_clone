#!/usr/bin/python3
"""
Unit tests for State class
"""

import unittest
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """
    Test suite for State class
    """

    def setUp(self):
        """Set up test instance"""
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.state)
        self.state = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    def test_name_type(self):
        """Test if 'name' attribute is of type str"""
        self.assertIsInstance(self.state.name, str)

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_relationships(self):
        """Test relationships with other classes"""
        city1 = City(state_id=self.state.id)
        city2 = City(state_id=self.state.id)
        storage.new(city1)
        storage.new(city2)
        storage.save()
        self.assertIn(city1, self.state.cities)
        self.assertIn(city2, self.state.cities)

    def test_additional_attributes(self):
        """Test additional attributes"""
        self.state.population = 1000000
        self.assertEqual(self.state.population, 1000000)

    def test_custom_method(self):
        """Test a custom method that operates on the State class"""
        self.state.update_population(1500000)
        self.assertEqual(self.state.population, 1500000)


if __name__ == "__main__":
    unittest.main()
