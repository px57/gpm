
from init.choices import choices_project_type
from kernel.path.find import find_directory_in_parent
from config.config import Config
from kernel.git.remote import get_remote_url
from kernel.git.remote import get_repository_name
import os 

def commandline__init():
    """
    This function is to initialize the command line
    """
    project_type = choices_project_type()

    root_path = find_directory_in_parent(".git", '.')
    gpm_path = os.path.join(root_path, ".gpm")

    if not os.path.exists(gpm_path):
        os.makedirs(gpm_path)

    config = Config()
    config.set("root_path", root_path)
    config.set("gpm_path", gpm_path)
    config.set("project_type", project_type["value"])
    config.set("repository_url", get_remote_url())
    config.set("name", get_repository_name())
    config.save()


    print ("The root path is: {}".format(root_path))
    print ("The gpm path is: {}".format(gpm_path))