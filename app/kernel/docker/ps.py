
from pprint import pprint

import os
import docker
import json
import inquirer 
import subprocess
import json


# Run the docker ps command with JSON output

 
                                                  
def docker_ps():
    """
        @description: 
    """
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{json .}}'],
        stdout=subprocess.PIPE,
        text=True
    )

    # Split output into lines and parse each line as JSON
    containers = [json.loads(line) for line in result.stdout.splitlines()]

    return containers

def docker_ps_json():
    """
        @description: 
    """
    containers = docker_ps()
    return json.dumps(containers, indent=4)

def choice_docker_container():
    """
        @description: 
    """
    # Récupération des conteneurs en cours d'exécution
    containers = docker_ps()

    # Affichage des conteneurs
    list_containers = []
    for i, container in enumerate(containers):
        list_containers.append(container['Names'])

    questions = [ 
        inquirer.List(
            'container', 
            message="Quel container souhaitez-vous utiliser ?", 
            choices=list_containers, 
            ), 
    ]    
 
    answers = inquirer.prompt(questions) 

    for container in containers:
        if container['Names'] == answers['container']:
            return container
    raise Exception("Container not found")