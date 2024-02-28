
import os
import docker
import json
import inquirer 
 
                                                  
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

def docker_ps_json():
    """
        @description: 
    """
    docker_ps = docker_ps()
    return json.dumps(docker_ps, indent=4)

def choice_docker_container():
    """
        @description: 
    """
    # Récupération des conteneurs en cours d'exécution
    containers = docker_ps()

    # Affichage des conteneurs
    list_containers = []
    for i, container in enumerate(containers):
        list_containers.append(container['Name'])

    questions = [ 
        inquirer.List(
            'container', 
            message="Quel container souhaitez-vous utiliser ?", 
            choices=list_containers, 
            ), 
    ]    
 
    answers = inquirer.prompt(questions) 

    for container in containers:
        if container['Name'] == answers['container']:
            return container
    raise Exception("Container not found")