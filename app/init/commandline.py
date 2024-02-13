
from init.choices import choices_project_type
from kernel.path.find import find_directory_in_parent
from config.config import Config
import os 

def commandline__init():
    """
    This function is to initialize the command line
    """
    # project_type = choices_project_type()

    project_type = {"value": "module"}
    # print ("The project type is: {}".format(project_type["value"]))

    root_path = find_directory_in_parent(".git", '.')
    gpm_path = os.path.join(root_path, ".gpm")

    if not os.path.exists(gpm_path):
        os.makedirs(gpm_path)

    config = Config()
    config.set("root_path", root_path)
    config.set("gpm_path", gpm_path)
    config.set("project_type", project_type["value"])
    config.save()


    print ("The root path is: {}".format(root_path))
    print ("The gpm path is: {}".format(gpm_path))