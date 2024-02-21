
import os 
from colorama import Fore, Style
from path.find import find_submodule_path

def commandline__all():
    """
    This function is to commit all submodules.
    """
    print (Fore.RED + ">>> Commit all the submodules..." + Style.RESET_ALL)
    pwd = os.getcwd()
    for submodule_path in find_submodule_path():
        print (Fore.RED + ">>> Commit the submodule: " + submodule_path + Style.RESET_ALL)
        choice = input("Do you want to commit the submodule? (y/n): ")
        if choice != "y":
            continue
        os.chdir(submodule_path)
        os.system('gpm commit')

    os.chdir(pwd)
    os.system('gpm commit')