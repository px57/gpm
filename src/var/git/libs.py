
import os
import datetime



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

def convert_time_string_to_datetime(time_string):
    # Define the format of the time string
    time_format = '%a %b %d %H:%M:%S %Y %z'

    # Convert the time string to a datetime object
    datetime_object = datetime.datetime.strptime(time_string, time_format)

    return datetime_object