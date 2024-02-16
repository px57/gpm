import os 

def is_django_project() -> bool:
    """
    This function is to check if the project is a django project
    """
    # -> check if the project is a django project
    return os.path.exists("manage.py")

def is_django_repository_name(repository_name: str) -> bool:
    """
    This function is to check if the repository name is a django repository name
    """
    # -> check if the repository name begin by dj- or django-
    return repository_name.startswith("dj-") or repository_name.startswith("django-")

def is_angular_project() -> bool:
    """
    This function is to check if the project is a angular project
    """
    # -> check if the project is a angular project
    return os.path.exists("angular.json")

def get_repository_name(repository_link: str) -> str:
    """
    This function is to get the repository name
    """
    # -> get the repository name, delete the .git and the last /
    return repository_link.split("/")[-1].replace(".git", "")
    
def commandline__clone():
    """
    This function is to clone.
    """
    repository = input("Enter the repository: ")
    repository_name = get_repository_name(repository)

    # -> observe if the repository name is adapted for this project. 
    # -> clone the repository in the postion adapted in the base.
    # -> load the gpm dependencies.
    # -> merge the requirements, for django of angular. 
    # -> run gpm init if the repository not exists