
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "kernel"))

import os
import docker
import json

# Colorama Imports
from colorama import Fore, Style

# Gpm Imports
from kernel.docker.ps import docker_ps
from kernel.docker.id import get_container_id

def is_root():
    return os.geteuid() == 0




def commandline__killall():
    """
    This function is to Kill all the containers.
    """
    if not is_root():
        args = ['sudo', sys.executable] + sys.argv 
        # Relancer le script avec sudo
        os.execvp('sudo', args)
        return 
    
    docker_list = docker_ps()
    # get list uid
    list_uid = [get_container_id(container) for container in docker_list]

    for uid in list_uid:
        print (Fore.RED + f">>> Kill the container {uid}..." + Style.RESET_ALL)
        os.system(f"docker stop {uid}")