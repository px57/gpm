
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

def is_not_root_execute_as_root():
    if not is_root():
        args = ['sudo', sys.executable] + sys.argv 
        # Relancer le script avec sudo
        os.execvp('sudo', args)
        return True

def commandline__db():
    """
    This function is to clone.
    """
    if is_not_root_execute_as_root():
        return
    
    if sys.argv[2] == 'pg_dumpall':
        return pg_dumpall()

def pg_dumpall():
    """
    This function is to send the pg_dumpall command.
    """
    if len(sys.argv) < 4:
        print("You must specify the filename")
        return
    
    if len(sys.argv) < 5:
        print("You must specify the dbusername")
        return
    
    filename = sys.argv[3]
    dbusername = sys.argv[4] 
    container = choice_docker_container()
    os.system(f"docker exec -it {container.get('ID')} pg_dumpall -U {dbusername} > {filename}")