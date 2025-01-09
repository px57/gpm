
from commit.all.commandline import commandline__all
from path.find import find_submodule_path
from config.config import Config
from colorama import Fore, Style, init
import os 
import sys

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)

def commandline__commit():
    """
    This function is to commit the changes.
    """
    if len(sys.argv) == 3:
        if sys.argv[2] == "all":
            return commandline__all()
        else: 
            print (Fore.RED + ">>> Error: " + sys.argv[2] + " is not a valid option." + Style.RESET_ALL)
            return
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
    commit(
        delete_all_migration = True
    )

def git_A():
    """
    This function is to add all the files.
    """
    print (Fore.RED + ">>> Add all the files..." + Style.RESET_ALL)
    os.system('git add -A')


def remove_in_git_all_migrations_file(delete_all_migration = False):
    """
    Remove migrations file in the git.
    """
    if not delete_all_migration:
        return
    
    # git rm --cached -r migrations
    print (Fore.RED + ">>> Remove all the migrations files..." + Style.RESET_ALL)
    if os.path.exists('migrations'):
        list_of_migrations = os.listdir('migrations')
        for migration in list_of_migrations:
            if migration == "__init__.py":
                continue
            cmd = 'git rm --cached -r migrations/' + migration
            print (cmd)
            os.system('git rm --cached -r migrations/' + migration) 
 

def commit(delete_all_migration = False):
    """
    This function is to commit the changes.
    """
    # Delete all the .pyc files
    os.system('sudo find . -name "*.pyc" -exec rm -f {} \;')

    git_A()
    remove_in_git_all_migrations_file(delete_all_migration=delete_all_migration)

    print (Fore.RED + ">>> Commit the changes..." + Style.RESET_ALL)
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
    This function is to connect-submodule.
    """
    print (Fore.RED + ">>> connect-submodule..." + Style.RESET_ALL)
    i = 0
    for submodule_path in find_submodule_path():
        git_path = os.path.join(submodule_path, ".git")
        gitdisable_path = os.path.join(submodule_path, ".gitdisable")

        if not os.path.exists(git_path):
            continue;
        
        i += 1
        print (Fore.GREEN + "connect-submodule(" + str(i) + "): " + submodule_path + Style.RESET_ALL)
        # moove the git_path to gitdisable_path

        if os.path.exists(gitdisable_path):
            # -> remove not empty directory
            os.system("rm -rf " + gitdisable_path)
        os.rename(git_path, gitdisable_path)

def submodule_unintegrate():
    """
    This function is to disconnect-submodule.
    """
    print (Fore.RED + ">>> disconnect-submodule..." + Style.RESET_ALL)
    i = 0
    for submodule_path in find_submodule_path():
        git_path = os.path.join(submodule_path, ".git")
        gitdisable_path = os.path.join(submodule_path, ".gitdisable")

        if os.path.exists(git_path):
            continue;
        
        i += 1
        print (Fore.GREEN + "disconnect-submodule(" + str(i) + "): " + submodule_path + Style.RESET_ALL)
        # moove the gitdisable_path to git_path
        os.rename(gitdisable_path, git_path)



    