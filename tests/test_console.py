#!/usr/bin/python3
""" test for console """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsoleShowCommand(unittest.TestCase):
    """Test cases for the show command in the console"""
    
    def setUp(self):
        self.console = HBNBCommand()
        self.test_id = "7d3e1daf-ef32-42dd-ae75-d9ebdb7a8f9c"
        self.obj = {"id": self.test_id, "name": "TestObject"}

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_show_command(self):
        """Test the show command with a stored object"""
        storage._FileStorage__objects[f"BaseModel.{self.test_id}"] = self.obj

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {self.test_id}")
            output = f.getvalue().strip()

        self.assertIn("TestObject", output)

class TestConsoleDestroyCommand(unittest.TestCase):
    """Test cases for the destroy command in the console"""
    
    def setUp(self):
        self.console = HBNBCommand()
        self.test_id = "7d3e1daf-ef32-42dd-ae75-d9ebdb7a8f9c"
        self.obj = {"id": self.test_id, "name": "TestObject"}

    def tearDown(self):
        self.console = None
        storage._FileStorage__objects = {}

    def test_destroy_command(self):
        """Test the destroy command by removing a stored object"""
        storage._FileStorage__objects[f"BaseModel.{self.test_id}"] = self.obj

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {self.test_id}")
            output = f.getvalue().strip()

        self.assertNotIn(self.test_id, storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
