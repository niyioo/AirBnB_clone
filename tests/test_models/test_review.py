#!/usr/bin/python3
"""
Unit tests for Review class
"""

import unittest
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """
    Test suite for Review class
    """

    def setUp(self):
        """Set up test instance"""
        self.review = Review()
        self.review.text = "Great experience"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.review)
        self.review = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.review, "text"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(original_updated_at, self.review.updated_at)

    def test_text_type(self):
        """Test if 'text' attribute is of type str"""
        self.assertIsInstance(self.review.text, str)

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_rating(self):
        """Test the rating attribute"""
        self.review.rating = 4
        self.assertEqual(self.review.rating, 4)


if __name__ == "__main__":
    unittest.main()
