
from init.choices import choices_project_type

def commandline__init():
    """
    This function is to initialize the command line
    """
    project_type = choices_project_type()
    print ("The project type is: {}".format(project_type["value"]))
    