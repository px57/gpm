"""
This file is used to install the package using pip.

1. create /var/projects/gpm/ directories and subdirectories.
2. Move the directories and subdirectories to /var/projects/gpm/ directory.
"""
import os

def create_directories():
    """
    This function is used to create the directories and subdirectories.
    """
    os.makedirs(
        '/var/projects/gpm/app/kernel/docker', 
        exist_ok=True
    )

def moove_directories():
    """
    This function is used to move the directories and subdirectories to /var/projects/gpm/ directory.
    """
    os.system(
        'cp -rf ./* /var/projects/gpm/'
    )

def create_command_file():
    """
    This function is used to create the command file.
    """
    os.system(
        'echo "gpm" > /usr/local/bin/gpm'
    )
    os.system(
        'chmod +x /usr/local/bin/gpm'
    )

def main():
    """
    This function is used to install the package using pip.
    """
    create_directories()
    moove_directories()
    create_command_file()

if __name__ == "__main__":
    main()

