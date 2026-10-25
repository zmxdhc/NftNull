# test_nftnull.py
"""
Tests for NftNull module.
"""

import unittest
from nftnull import NftNull

class TestNftNull(unittest.TestCase):
    """Test cases for NftNull class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftNull()
        self.assertIsInstance(instance, NftNull)

    def test_run_method(self):
        """Test the run method."""
        instance = NftNull()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
