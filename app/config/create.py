
import os
from kernel.path.find import find_directory_in_parent
from config.find import find_gpm_path

def if_gpm_path_not_exists_create():
    """
    This function is to create the .gpm directory
    """
    gpm_path = find_gpm_path()

    if os.path.exists(gpm_path):
       return gpm_path

    os.makedirs(gpm_path)
    return gpm_path

def if_basejson_not_exists_create():
    """
    This function is to create the base.json file
    """
    gpm_path = find_gpm_path()
    base_file = os.path.join(gpm_path, "base.json")
    if os.path.exists(base_file):
        return base_file

    with open(base_file, "w") as f:
        f.write("{}")
    return base_file
