
import subprocess
import os

def has_modification(git_path: str):
    """
    This function is to check if the project has modification.

    Args:
    - git_path: the git path.   
    """
    # Se déplacer dans le répertoire du dépôt Git
    original_cwd = subprocess.os.getcwd()

    # Exécuter `git status --porcelain` pour voir s'il y a des modifications non commit
    result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True)

    # Revenir au répertoire original
    subprocess.os.chdir(original_cwd)

    # Analyser le résultat
    if result.stdout:
        print("Il y a des modifications non commit.")
        print(result.stdout)
        return True
    else:
        print("Aucune modification non commit.")
        return False