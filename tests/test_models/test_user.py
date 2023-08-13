#!/usr/bin/python3
"""
Unit tests for User class
"""

import unittest
import datetime
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
    """
    Test suite for User class
    """

    def setUp(self):
        """Set up test instance"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john@example.com"
        self.user.password = "password"

    def tearDown(self):
        """Clean up after test"""
        storage.delete(self.user)
        self.user = None

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))

    def test_save(self):
        """Test the save method"""
        original_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(original_updated_at, self.user.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['email'], "john@example.com")
        self.assertEqual(user_dict['password'], "password")

    def test_reload(self):
        """Test the reload method"""
        storage.save()
        original_updated_at = self.user.updated_at
        storage.reload()
        loaded_user = storage.get(User, self.user.id)
        self.assertEqual(original_updated_at, loaded_user.updated_at)

    def test_created_at(self):
        """Test if created_at is properly set"""
        self.assertTrue(hasattr(self.user, "created_at"))

    def test_updated_at_type(self):
        """Test if updated_at is of datetime type"""
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_full_name(self):
        """Test the full_name method"""
        full_name = self.user.full_name()
        expected_full_name = "John Doe"
        self.assertEqual(full_name, expected_full_name)

    def test_email_format(self):
        """Test if email follows a valid format"""
        valid_emails = [
            "user@example.com",
            "john.doe@example.co.uk",
            "test_user123@example.org"
        ]
        invalid_emails = [
            "invalid_email",
            "user@example",
            "user@example..com"
        ]
        for email in valid_emails:
            self.assertTrue(self.user.validate_email_format(email))
        for email in invalid_emails:
            self.assertFalse(self.user.validate_email_format(email))


if __name__ == "__main__":
    unittest.main()
