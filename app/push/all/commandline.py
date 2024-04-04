
import os 
from colorama import Fore, Style
from path.find import find_submodule_path
from kernel.git.status import has_modification

def has_commit_not_pushed(submodule_path):
    """
    Observe if the submodule has commit not pushed.
    """
    os.chdir(submodule_path)
    o = os.system('gpm status')
    print (o)
    os.chdir('..')
    return o != 0


def commandline__all():
    """
    This function is to Push all submodules.
    """
    print (Fore.RED + ">>> Push all the submodules..." + Style.RESET_ALL)
    pwd = os.getcwd()
    for submodule_path in find_submodule_path():
        # if not has_commit_not_pushed(submodule_path):
        #     continue
        submodule_name = os.path.basename(submodule_path)
        print (Fore.RED + ">>> Push the submodule: " + submodule_name.upper() + Style.RESET_ALL)
        # choice = input("Do you want to push the " + submodule_name.upper() + "? (y/n): ")
        # if choice != "y":
        #     continue
        os.chdir(submodule_path)
        os.system('gpm push')
        os.chdir(pwd)

    if not has_modification(pwd):
        return
    os.chdir(pwd)
    os.system('gpm push')