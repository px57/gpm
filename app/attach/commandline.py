
# Kernel import
from kernel.docker.ps import docker_ps_json
from kernel.docker.ps import choice_docker_container
from kernel.docker.attach import docker_attach

# Python import
import pprint
import os
import subprocess
import sys

def is_root():
    return os.geteuid() == 0


def commandline__attach():
    """
    This function is to clone.
    """
    if not is_root():
        args = ['sudo', sys.executable] + sys.argv 
        # Relancer le script avec sudo
        os.execvp('sudo', args)
        return 
    
    print (sys.argv)
    if '--json' in sys.argv:
        print(docker_ps_json())
        return
    
    # result = subprocess.run(["sudo", "-S"] + commandline, capture_output=True, text=True, input='t9fect9fec\n')
    container = choice_docker_container()
    docker_attach(container)