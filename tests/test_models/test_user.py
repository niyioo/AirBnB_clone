#!/usr/bin/python3
import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john@example.com"
        self.user.password = "password"

    def tearDown(self):
        storage.delete(self.user)
        self.user = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))

    def test_save(self):
        original_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(original_updated_at, self.user.updated_at)

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['email'], "john@example.com")
        self.assertEqual(user_dict['password'], "password")

    def test_reload(self):
        storage.save()
        original_updated_at = self.user.updated_at
        storage.reload()
        loaded_user = storage.get(User, self.user.id)
        self.assertEqual(original_updated_at, loaded_user.updated_at)

if __name__ == "__main__":
    unittest.main()
