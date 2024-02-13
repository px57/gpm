
import os
from config.find import find_gpm_path
import json

class Config:
    """
    Gpm Configurations
    """

    def __init__(self):
        """
        This is the constructor
        """
        self.root_path = find_gpm_path()        
        self.load()

    @property
    def base_path(self):
        """
        This function is to get the base path
        """
        return self.root_path + "/base.json"
     

    def load(self):
        """
        This function is to load the base.json file
        """
        if not os.path.exists(self.base_path):
            return self

        with open(self.base_path, "r") as f:
            self.base = f.read()

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

    def json(self):
        """
        This function is to get the base.json file
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
        return json.dumps(dictionary)

    def save(self):
        """
        This function is to save the base.json file
        """
        with open(self.base_path, "w+") as f:
            f.write(self.json())
