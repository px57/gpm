
import os
from kernel.path.find import find_directory_in_parent

def find_gpm_path():
    """
    This function is to find the gpm path
    """
    root_path = find_directory_in_parent(".git", '.')
    gpm_path = os.path.join(root_path, ".gpm")
    return gpm_path