
from dock.killall.commandline import commandline__killall
import sys

def commandline__docker():
    """
    This function is to Push all submodules.
    """
    if sys.argv[2] == 'killall':
        return commandline__killall()