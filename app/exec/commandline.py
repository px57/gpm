
from kernel.docker.ps import choice_docker_container
from kernel.docker.exec import docker_exec_bash
import pprint
import os
import subprocess
import sys

def is_root():
    return os.geteuid() == 0


def commandline__exec():
    """
    This function is to clone.
    """
    if not is_root():
        args = ['sudo', sys.executable] + sys.argv 
        # Relancer le script avec sudo
        os.execvp('sudo', args)
        return 
    
    # result = subprocess.run(["sudo", "-S"] + commandline, capture_output=True, text=True, input='t9fect9fec\n')
    container = choice_docker_container()
    docker_exec_bash(container)