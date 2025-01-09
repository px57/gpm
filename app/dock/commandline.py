
from dock.killall.commandline import commandline__killall
from dock.rm.commandline import commandline__rm

import sys

def commandline__docker():
    """
    This function is to Push all submodules.
    """
    if sys.argv[2] == 'killall':
        return commandline__killall()
    elif sys.argv[2] == 'rm':
        return commandline__rm()
    