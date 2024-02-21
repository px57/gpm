
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
        os.chdir(submodule_path)
        os.system('gpm commit')

    os.chdir(pwd)
    os.system('gpm commit')