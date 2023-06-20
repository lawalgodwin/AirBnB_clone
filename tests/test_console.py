#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unit test for the console app
    """

    def setUp(self):
        """Basic setup before each testcase"""
        self.cli = HBNBCommand()
        self.output = StringIO()
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def tearDown(self):
        """Basic cleanup after each test case"""
        self.output.close()

    def test_create_command(self):
        """
        test for object creation
        """
        with patch('sys.stdout', self.output):
            self.cli.onecmd("create")
        nonameoutput = self.output.getvalue().strip()
        self.assertEqual(nonameoutput, self.err[0])

    def test_destroy_command(self, nr=None):
        """test for destroy command"""

    def test_show_command(self):
        """test for show command"""

    def test_update_command(self):
        """test for the update command"""
    def test_quit_command(self):
        """test for Quit command"""
        with patch('sys.stdout', self.output):
            self.cli.onecmd("quit")
        output = self.output.getvalue().strip()
        self.assertEqual(output, "Exiting...")


if __name__ == '__main__':
    unittest.main()
