
import os 
from colorama import Fore, Style
from path.find import find_submodule_path

def has_modification(git_path: str):
    """
    This function is to check if the project has modification.

    Args:
    - git_path: the git path.   
    """
    pwd = os.getcwd()
    os.chdir(git_path)
    a = os.system('git status')
    os.chdir(pwd)
    if a == 0:
        return False
    else:
        return True


def commandline__all():
    """
    This function is to commit all submodules.
    """
    print (Fore.RED + ">>> Commit all the submodules..." + Style.RESET_ALL)
    pwd = os.getcwd()
    for submodule_path in find_submodule_path():
        if not has_modification(submodule_path):
            continue
        submodule_name = os.path.basename(submodule_path)
        print (Fore.RED + ">>> Commit the submodule: " + submodule_name.upper() + Style.RESET_ALL)
        choice = input("Do you want to commit the " + submodule_name.upper() + "? (y/n): ")
        if choice != "y":
            continue
        os.chdir(submodule_path)
        os.system('gpm commit')

    os.chdir(pwd)
    os.system('gpm commit')