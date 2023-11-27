


def code__linux(command_name: str, executable_path: str):
    """
        @description:
        @param.command_name: The name of the new command
        @param.executable_path: The path to the executable
    """
    return f"""
#!/usr/bin/env python3

import os
import sys

def main():
    print ('grosse salope ')
    print ('{executable_path} ' + ' '.join(sys.argv[1:]))
    os.system('{executable_path} ' + ' '.join(sys.argv[1:]))


main()
"""
import os

def has_permission__linux(path: str):
    """
        @description:
    """
    import os
    return os.access(path, os.X_OK)

def not_has_permission__linux(path: str):
    """
        @description:
    """
    return not has_permission__linux(path)

def create_command_bridge__linux(
        command_name: str, 
        executable_path: str
):
    """
        @description:
        @param.command_name: The name of the new command
        @param.executable_path: The path to the executable
    """
    code = code__linux(command_name, executable_path)
    path = f'/usr/bin/{command_name}'

    print (path)
    try: 
        with open(path, 'w') as f:
            f.write(code)
    except: 
        raise Exception('Permission denied, try with sudo.')
    
    os.system(f'sudo chmod +x {path}')
    
def create_command_bridge__windows(
        command_name: str, 
        executable_path: str
):
    """
        @description:
        @param.command_name: The name of the new command
        @param.executable_path: The path to the executable
    """