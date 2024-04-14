
from modules.connect.commandline import commandline__connect
from modules.disconnect.commandline import commandline__disconnect

import sys
import os 

description = """
This module contains the main modules of the application.
"""
def commandline__modules():
    """
    This function is to clone.
    
    """
    if len(sys.argv) == 2:
        print(description)
        return
    
    if sys.argv[2] == "connect":
        return commandline__connect() 
    elif sys.argv[2] == "disconnect":
        return commandline__disconnect()