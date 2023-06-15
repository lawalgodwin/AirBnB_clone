#!/usr/bin/python3
"""A test script for the amenity module"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for the amenity class"""

    def setUp(self):
        # Create an instance of Amenity for testing
        self.amenity = Amenity()

    def test_attributes(self):
        # Test the initial attribute values
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        # Test if Amenity inherits from BaseModel
        self.assertIsInstance(self.amenity, BaseModel)

    def test_setting_attributes(self):
        # Test setting attribute values
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
