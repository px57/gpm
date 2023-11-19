import unittest
from unittest import TestCase
from var import Version

class VersionVarTest(TestCase):
    """
        @description: 
    """

    def test_available_version(self):
        """
            @description: 
        """
        version = Version('1.22.234 (main)')
        self.assertEqual(version.branch, 'main')
        self.assertEqual(version.num, '1.22.234')

    def test_next_version(self):
        """
            @description: Test change the version.   
        """
        version = Version('0.0.0 (main)')
        for i in range(1000000):
            version.next()

if __name__ == '__main__':
    unittest.main()