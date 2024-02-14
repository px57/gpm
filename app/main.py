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
from help.commandline import commandline__help
from commit.commandline import commandline__commit
from editable.commandline import commandline__editable

from commit.commandline import submodule_integrate 

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
    elif sys.argv[1] == "commit":
        if len(sys.argv) == 2:
            return commandline__commit()
        elif sys.argv[2] == "manual":
            return submodule_integrate()
    elif sys.argv[1] == "editable":
        return commandline__editable()
    else:
        return commandline__help()

if __name__ == "__main__":
    main()