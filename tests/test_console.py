#!/usr/bin/python3
""" Test for console """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsoleUpdateCommand(unittest.TestCase):
    """Test cases for the update command in the console"""

    def setUp(self):
        self.console = HBNBCommand()
        self.test_id = "7d3e1daf-ef32-42dd-ae75-d9ebdb7a8f9c"
        self.obj = {"id": self.test_id, "name": "TestObject"}

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_update_command(self):
        """Test the update command by modifying a stored object"""
        storage._FileStorage__objects[f"BaseModel.{self.test_id}"] = self.obj

        with patch('sys.stdout', new=StringIO()) as f:
            update_cmd = f"update BaseModel {self.test_id} name NewName"
            self.console.onecmd(update_cmd)
            output = f.getvalue().strip()

        expected_value = storage._FileStorage__objects[
            f"BaseModel.{self.test_id}"]["name"]
        self.assertIn("NewName", expected_value)


class TestConsoleCreateCommand(unittest.TestCase):
    """Test cases for the create command in the console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_create_command(self):
        """Test the create command by creating a new object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        self.assertIn("id", storage._FileStorage__objects[output])
        self.assertIsInstance(storage._FileStorage__objects[output], dict)


class TestConsoleCountCommand(unittest.TestCase):
    """Test cases for the count command in the console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_count_command(self):
        """Test the count command by counting stored objects"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            output = f.getvalue().strip()

        self.assertEqual(int(output), 0)

        # Create some objects
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            output = f.getvalue().strip()

        self.assertEqual(int(output), 3)


class TestConsoleAllCommand(unittest.TestCase):
    """Test cases for the all command in the console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_all_command(self):
        """Test the all command by listing all stored objects"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            output = f.getvalue().strip()

        self.assertEqual(output, "[]")

        # Create some objects
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        self.assertIn("id", output)


if __name__ == '__main__':
    unittest.main()
