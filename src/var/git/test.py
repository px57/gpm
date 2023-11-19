
from libs import find_gitrepository
import unittest

REPOSITORY_LIST = '/home/david/Bureau/'
repository_list = find_gitrepository(REPOSITORY_LIST)

class TestGitManager(unittest.TestCase):
    """
        @description: 
    """

    def test_getchangelist(self):
        """
            @description: 
        """
        print (repository_list)

unittest.main()