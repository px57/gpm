
import os


def create_command_bridge(
    command_name: str, 
    executable_path: str
):
    """
        @description:
        @param.command_name: The name of the new command
        @param.executable_path: The path to the executable
    """
    from tools.create_command_bridge import create_command_bridge__linux, create_command_bridge__windows
    if os.name == 'posix':
        create_command_bridge__linux(
            command_name, 
            executable_path
        )
    elif os.name == 'nt':
        create_command_bridge__windows(
            command_name, 
            executable_path
        )
    else:
        raise Exception('Unsupported OS: ' + os.name)