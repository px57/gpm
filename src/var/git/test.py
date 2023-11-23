
from libs import find_gitrepository
import unittest

REPOSITORY_LIST = '/home/david/Bureau/'
repository_list = find_gitrepository(REPOSITORY_LIST)

class TestGitManager(unittest.TestCase):
    """
        @description: 
    """

    def test_commit_list(self):
        """
            @description: 
        """
        for repository in repository_list:
            repository.commit_list()

    def test_change_list(self):
        """
            @description: 
        """
        for repository in repository_list:
            repository.get_files_change()

    def test_getbranch(self):
        """
            @description: 
        """
        for repository in repository_list:
            repository.branch

    def test_branch_list(self):
        """
            @description: 
        """
        for repository in repository_list:
            repository.branch_list

    def test_create_branch(self):
        """
            @description: 
        """
        for repository in repository_list:
            repository.create_branch('created_by_test')


unittest.main()