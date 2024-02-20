
# from dj.makemigrations.commandline import commandline__expurge_makemigrations
from dj.expurge_makemigrations.commandline import commandline__expurge_makemigrations

import sys

def commandline__django():
    """
    This function is to commit the changes.
    """
    if sys.argv[2] == "expurge_makemigrations":
        return commandline__expurge_makemigrations()
    sys.exit(0)