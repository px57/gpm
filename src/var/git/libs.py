
import os


def has_gitignore_tolistdir(listdir: list):
    """
        @description: 
    """
    return '.gitignore' in listdir

def has_git_tolistdir(listdir: list): 
    """
        @description: 
    """
    return '.git' in listdir

def find_gitrepository(base_path: str):
    """
        @description: 
    """
    from var import GitRepository
    repository_list = []
    for root, dirs, files in os.walk(base_path):
        if has_git_tolistdir(files):
            repository_list.append(GitRepository(root))
    return repository_list