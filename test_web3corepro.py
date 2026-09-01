# test_web3corepro.py
"""
Tests for Web3CorePro module.
"""

import unittest
from web3corepro import Web3CorePro

class TestWeb3CorePro(unittest.TestCase):
    """Test cases for Web3CorePro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3CorePro()
        self.assertIsInstance(instance, Web3CorePro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3CorePro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
