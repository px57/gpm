
from kernel.docker.ps import choice_docker_container
from kernel.docker.attach import docker_attach
import pprint
import os

def commandline__attach():
    """
    This function is to clone.
    """
    container = choice_docker_container()
    docker_attach(container)