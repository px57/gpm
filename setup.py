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
    # os.makedirs(
    #     '/var/projects/gpm/app/kernel/docker', 
    #     exist_ok=True
    # )
    os.system(
        'sudo mkdir -p /var/projects/gpm/app/kernel/docker'
    )


def moove_directories():
    """
    This function is used to move the directories and subdirectories to /var/projects/gpm/ directory.
    """
    os.system(
        'sudo mkdir -p /var/projects',
    )

    os.system(
        'sudo mkdir -p /var/projects/gpm',
    )

    os.system(
        'sudo cp -rf ./* /var/projects/gpm/'
    )

    # chmod -R 777 /var/projects/gpm
    os.system(
        'sudo chmod -R 777 /var/projects/gpm'
    )

def create_command_file():
    """
    This function is used to create the command file.
    """
    file = """#!/usr/bin/env python3
import os
import sys

argv = sys.argv[1:]
command = 'python3 /var/projects/gpm/app/main.py ' + ' '.join(argv)
os.system(command)
"""
    os.system('sudo touch /usr/local/bin/gpm')
    os.system('sudo chmod 777 /usr/local/bin/gpm')

    with open('/usr/local/bin/gpm', 'w') as f:
        f.write(file)

    # Delete the first "\n" in the /user/local/bin/gpm

    os.system(
        'chmod +x /usr/local/bin/gpm'
    )

def save_chatgpt_api_key():
    """

    """
    key = input("Enter your OpenAI ChatGPT API key: ")

    os.system(
        'mkdir -p ~/.config/commitgpt'
    )
    # mkdir -p ~/.config/commitgpt

    os.system(
        'touch ~/.config/commitgpt/config.toml'
    )

    # touch ~/.config/commitgpt/config.toml

    os.system(
        f'echo api_key = \"{key}\" > ~/.config/commitgpt/config.toml'
    )
    # echo 'api_key = "YOUR_OPENAI_API_KEY"' > ~/.config/commitgpt/config.toml

def setup_requirements():
    """ 
    This function is used to install the requirements.
    """
    # Install rust.
    os.system(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    )

    # Install cargo.
    os.system(
        'sudo apt  install cargo '
    )

    # Python requirements
    os.system(
        'pip3 install -r requirements.text'
    )

    # Cargo requirements
    os.system(
        'export PATH="$HOME/.cargo/bin:$PATH"'
    )
    os.system(
        'sudo cargo install commitgpt'
    )

def main():
    """
    This function is used to install the package using pip.
    """
    setup_requirements()
    create_directories()
    moove_directories()
    create_command_file()
    save_chatgpt_api_key()

if __name__ == "__main__":
    main()

