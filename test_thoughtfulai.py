import unittest
from thoughtfulai import is_bulky, is_heavy, sort

class TestPackageSorter(unittest.TestCase):
    
    def test_is_bulky(self):
        # Bulky due to volume
        self.assertTrue(is_bulky(200, 200, 200))  # Volume = 8,000,000 cm³
        # Bulky due to dimension
        self.assertTrue(is_bulky(150, 50, 50))  # Width >= 150
        # Not bulky
        self.assertFalse(is_bulky(100, 100, 99))

    def test_is_heavy(self):
        # Heavy
        self.assertTrue(is_heavy(25))  # Mass >= 20 kg
        # Not heavy
        self.assertFalse(is_heavy(10))  # Mass < 20 kg

    def test_sort(self):
        # Standard package
        self.assertEqual(sort(100, 100, 99, 10), "STANDARD")
        # Special package (bulky only)
        self.assertEqual(sort(200, 50, 20, 10), "SPECIAL")
        # Special package (heavy only)
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        # Rejected package (bulky and heavy)
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")
        # Edge case: both bulky and heavy
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

if __name__ == "__main__":
    unittest.main()
