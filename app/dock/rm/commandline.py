
from kernel.docker.ps import choice_docker_container
from kernel.docker.id import get_container_id

from dock.killall.commandline import commandline__killall

import sys
import os

def is_root():
    return os.geteuid() == 0

def commandline__rm():
    """
    This function is to Push all submodules.
    """
    if not is_root():
        args = ['sudo', sys.executable] + sys.argv 
        # Relancer le script avec sudo
        os.execvp('sudo', args)
        return 

    # -> 
    container = choice_docker_container()
    os.system('sudo docker rm -f ' + get_container_id(container))