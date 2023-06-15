#!/usr/bin/python3
"""A test script for the amenity module"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case for the state class"""

    def setUp(self):
        # Create an instance of State for testing
        self.state = State()

    def test_attributes(self):
        # Test the initial attribute values
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        # Test if Amenity inherits from BaseModel
        self.assertIsInstance(self.state, BaseModel)

    def test_setting_attributes(self):
        # Test setting attribute values
        self.state.name = "Swimming Pool"
        self.assertEqual(self.state.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
