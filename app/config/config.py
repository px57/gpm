
import os
from config.find import find_gpm_path
import pprint
import json

from colorama import Fore, Style, init

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)

class Config:
    """
    Gpm Configurations
    """

    def __init__(self, path_now='./'):
        """
        This is the constructor
        :param path_now: the path
        """
        self.root_path = find_gpm_path() 
        self.load()

    @property
    def base_path(self, path_now='./'):
        """
        This function is to get the base path
        :param path_now: the path
        """
        return find_gpm_path() + "/base.json"
     

    def load(self):
        """
        This function is to load the base.json file
        """
        if not os.path.exists(self.base_path):
            return self

        base = {}
        with open(self.base_path, "r") as f:
            base = f.read()
    
        base = json.loads(base)
        for key in base:
            try:
                setattr(self, key, base[key])
            except:
                pass
        return self
    
    def create(self):
        """
        This function is to create the base.json file
        """
        if not os.path.exists(self.base_path):
            with open(self.base_path, "w") as f:
                f.write("{}")
        return self

    def set(self, key, value):
        """
        This function is to set the value of the key
        :param key: the key
        :param value: the value
        """
        setattr(self, key, value)
        return self

    def dict(self):
        """
        This function is to get the dictionary
        """
        # get the list of the attributes
        attributes = dir(self)
        # remove the private attributes
        attributes = [a for a in attributes if not a.startswith("_")]
        # delete the callables
        attributes = [a for a in attributes if not callable(getattr(self, a))]
        # create the dictionary
        dictionary = {}
        for a in attributes:
            dictionary[a] = getattr(self, a)
        # return the dictionary
        return dictionary

    def json(self):
        """
        This function is to get the base.json file
        """
        return json.dumps(self.dict(), indent=4)

    def save(self):
        """
        This function is to save the base.json file
        """
        with open(self.base_path, "w+") as f:
            f.write(self.json())

    def status(self):
        """
        This function is to show the status
        """

        order = [
            'name',
            'project_type',
            'repository_url',
            'root_path',
            'gpm_path',
            'base_path'
        ]
        for key in order:
            if not hasattr(self, key):
                continue
            self.status_show_key(key)

        for key in self.dict().keys():
            if key in order:
                continue
            self.status_show_key(key)

    def status_show_key(self, key):
        """
        This function is to show the status of the key
        :param key: the key
        """
        value = getattr(self, key)
        show = Fore.GREEN + key + Style.RESET_ALL + ": " + str(value)
        print(show)

    def is_project(self):
        """
        This function is to check if the project
        """
        if not hasattr(self, "project_type"):
            return False
        project_type = getattr(self, "project_type")
        return project_type == "project"
    
    def is_module(self):
        """
        This function is to check if the module
        """
        if not hasattr(self, "project_type"):
            return False
        project_type = getattr(self, "project_type")
        return project_type == "module"
        