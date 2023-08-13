#!/usr/bin/python3
import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        storage.delete(self.state)
        self.state = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_save(self):
        original_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
