
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "kernel"))

import os
import docker
import json
from colorama import Fore, Style

def is_root():
    return os.geteuid() == 0


def docker_ps():
    """
        @description: 
    """
    # Connexion au client Docker
    client = docker.from_env()

    # Récupération des conteneurs en cours d'exécution
    containers = client.containers.list()

    # Conversion des conteneurs en format JSON
    json_data = []
    for container in containers:
        json_data.append(container.attrs)

    return json_data

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
    list_uid = [container['Id'] for container in docker_list]
    print (list_uid)
    for uid in list_uid:
        print (Fore.RED + f">>> Kill the container {uid}..." + Style.RESET_ALL)
        os.system(f"docker stop {uid}")