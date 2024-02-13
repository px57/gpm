
from colorama import Fore, Style, init
import os 

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)

def commandline__commit():
    """
    This function is to commit the changes.
    """
    print (Fore.RED + ">>> Integrate submodule repository..." + Style.RESET_ALL)
    print (Fore.RED + ">>> Commit the changes..." + Style.RESET_ALL)
    commit_command_line()


def commit_command_line():
    """
    This function is to commit the changes.
    """
    os.system('git add -A')
    os.system('commitgpt --suggestions 7 --max-tokens 100 ""')
