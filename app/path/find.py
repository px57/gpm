"""

"""

import os
from config.find import find_gpm_path

def find_submodule_path():
    """
    This function is to find the submodule path
    """
    submodule_list = []
    root_path = find_gpm_path().replace("/.gpm", "")

    for root, dirs, files in os.walk(root_path):
        # -> has .gpm directory
        # print (dirs)
        if ".gpm" not in dirs:
            continue

        if root == root_path:
            continue
        submodule_list.append(root)

    return submodule_list
