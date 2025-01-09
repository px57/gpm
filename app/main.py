# -*- coding: utf-8 -*-
"""
The project is create an applitacion to manage the code source between multiple projects.
Is the cascading source code   CSC (Cascading Source Code)
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ""))
sys.path.append(os.path.join(os.path.dirname(__file__), "kernel"))

from init.commandline import commandline__init
from status.commandline import commandline__status
from help.commandline import commandline__help
from commit.commandline import commandline__commit
from editable.commandline import commandline__editable
from attach.commandline import commandline__attach
from exec.commandline import commandline__exec
from makemigrations.commandline import commandline__makemigrations
from dj.commandline import commandline__django
from push.commandline import commandline__push
from dock.commandline import commandline__docker
from modules.commandline import commandline__modules
from db.commandline import commandline__db

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
    elif sys.argv[1] == "db":
        return commandline__db()
    elif sys.argv[1] == "status":
        return commandline__status()
    elif sys.argv[1] == "commit":
        return commandline__commit()
    elif sys.argv[1] == "editable":
        return commandline__editable()
    elif sys.argv[1] == "push":
        return commandline__push()
    elif sys.argv[1] == "pull":
        return os.system("git pull")
    elif sys.argv[1] == "attach":
        return commandline__attach()
    elif sys.argv[1] == "exec":
        return commandline__exec()
    elif sys.argv[1] == "makemigrations":
        return commandline__makemigrations()
    elif sys.argv[1] == "dj":
        return commandline__django()
    elif sys.argv[1] == "docker":
        return commandline__docker()
    elif sys.argv[1] == "modules":
        return commandline__modules()
    else:
        return commandline__help()

if __name__ == "__main__":
    main()