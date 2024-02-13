# -*- coding: utf-8 -*-
"""
The project is create an applitacion to manage the code source between multiple projects.
Is the cascading source code   CSC (Cascading Source Code)
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ""))
from init.commandline import commandline__init
from status.commandline import commandline__status

def commandline__help():
    """
    This function is to show the help
    """
    print ("This is the help")
    print ('gpm init ')

def main():
    """
    This is the main function
    """
    if len(sys.argv) == 1:
        return commandline__help()
    
    if sys.argv[1] == "init":
        return commandline__init()
    elif sys.argv[1] == "help":
        return commandline__help()
    elif sys.argv[1] == "status":
        return commandline__status()
    else:
        return commandline__help()


if __name__ == "__main__":
    main()