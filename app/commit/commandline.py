
from colorama import Fore, Style, init
import os 

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)

def commandline__commit():
    """
    This function is to commit the changes.
    """
    print (Fore.RED + "Commit the changes" + Style.RESET_ALL)

    os.system('git add -A')
    os.system('commitgpt --suggestions 7 --max-tokens 100 ""')
    # git add -A ; commitgpt --suggestions 7 --max-tokens 100 ""