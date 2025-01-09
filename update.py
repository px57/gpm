
import sys

sys.path.append('.')

from setup import create_directories, moove_directories, create_command_file

def main():
    """
    This function is used to install the package using pip.
    """
    create_directories()
    moove_directories()
    create_command_file()

if __name__ == "__main__":
    main()
