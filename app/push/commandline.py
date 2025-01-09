
from colorama import Fore, Style
from push.all.commandline import commandline__all
import sys
import os

def commandline__push():
    """
    This function is to push the changes.
    """
    print (Fore.RED + ">>> Push the changes..." + Style.RESET_ALL)
    if len(sys.argv) == 3:
        if sys.argv[2] == "all":
            return commandline__all()
        else: 
            print (Fore.RED + ">>> Error: " + sys.argv[2] + " is not a valid option." + Style.RESET_ALL)
            return
    os.system('git push')