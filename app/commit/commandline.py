
from path.find import find_submodule_path
from config.config import Config
from colorama import Fore, Style, init
import os 

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)

def commandline__commit():
    """
    This function is to commit the changes.
    """
    config = Config()
    if config.is_project():
        commitcommand___commit__project()
    elif config.is_module():
        commitcommand___commit__module()

def commitcommand___commit__project():
    """
    This function is to commit the changes of the project.
    """
    submodule_integrate()
    commit()
    submodule_unintegrate()

def commitcommand___commit__module():
    """
    This function is to commit the changes of the submodule.
    """
    commit()

def commit():
    """
    This function is to commit the changes.
    """
    print (Fore.RED + ">>> Commit the changes..." + Style.RESET_ALL)
    os.system('git add -A')
    a = os.system('commitgpt --suggestions 7 --max-tokens 100 ""')
    print ('commitgpt >> ' + str(a))
    if a == 256:
        print (Fore.RED + ">>> Commit failed." + Style.RESET_ALL)
        commit_message = input("Enter the commit message: ")
        os.system('git commit -m "' + commit_message + '"')
    else:
        print (Fore.GREEN + ">>> Commit done." + Style.RESET_ALL)


def submodule_integrate():
    """
    This function is to integrate the submodule.
    """
    print (Fore.RED + ">>> Integrate the submodule..." + Style.RESET_ALL)
    for submodule_path in find_submodule_path():
        git_path = os.path.join(submodule_path, ".git")
        gitdisable_path = os.path.join(submodule_path, ".gitdisable")

        if not os.path.exists(git_path):
            continue;
        
        print (Fore.GREEN + "Integrate-submodule: " + submodule_path + Style.RESET_ALL)
        # moove the git_path to gitdisable_path
        os.rename(git_path, gitdisable_path)

def submodule_unintegrate():
    """
    This function is to unintegrate the submodule.
    """
    print (Fore.RED + ">>> Unintegrate the submodule..." + Style.RESET_ALL)
    for submodule_path in find_submodule_path():
        git_path = os.path.join(submodule_path, ".git")
        gitdisable_path = os.path.join(submodule_path, ".gitdisable")

        if os.path.exists(git_path):
            continue;
        
        print (Fore.GREEN + "Unintegrate-submodule: " + submodule_path + Style.RESET_ALL)
        # moove the gitdisable_path to git_path
        os.rename(gitdisable_path, git_path)

def commandline__commit__all():
    """
    This function is to commit all submodules.
    """
    print ('save the chdir >> ' + os.getcwd())
    print ('get all submodules')
    submodules = find_submodule_path()
    print ('submodules >> ' + str(submodules))
    # for submodule in submodules:
    #     print ('submodule >> ' + submodule)
    #     os.chdir(submodule)
    #     commit()

    print ('restore the chdir >> ' + os.getcwd())
    # os.chdir(os.path.join(os.getcwd(), ".."))
    print ('commit')


    