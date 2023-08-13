#!/usr/bin/python3
import unittest
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()
        self.review.text = "Great experience"

    def tearDown(self):
        storage.delete(self.review)
        self.review = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "text"))

    def test_save(self):
        original_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(original_updated_at, self.review.updated_at)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
