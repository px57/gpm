
import subprocess
import os

def has_modification(git_path: str):
    """
    This function is to check if the project has modification.

    Args:
    - git_path: the git path.   
    """
    # Se déplacer dans le répertoire du dépôt Git
    # os.chdir(git_path)

    # Exécuter `git status --porcelain` pour voir s'il y a des modifications non commit
    result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True)

    # Revenir au répertoire original
    subprocess.os.chdir(git_path)

    # Analyser le résultat
    if result.stdout:
        # print("Il y a des modifications non commit.")
        # print(result.stdout)
        stdout = result.stdout
        clear_stdout = []
        for line in stdout.splitlines():
            if '.gitdisable/' in line:
                continue
            if 'migrations/' in line:
                continue
            clear_stdout.append(line)
        
        print ('#########################################')
        for line in clear_stdout:
            print(line)
        print ('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        return len(clear_stdout) > 1
    else:
        print("Aucune modification non commit.")
        return False