from colorama import Fore, Style, init

# Initialiser colorama pour s'assurer qu'il fonctionne bien dans tous les terminaux
init(autoreset=True)


def commandline__help():
    """
    This function is to show the help
    """
    print (Fore.RED + "*** Welcome to Gpm ***" + Style.RESET_ALL)

    help_list = {
        "init": "This command is to initialize the gpm",
        "status": "This command is to show the status of the gpm",
        "help": "This command is to show the help",
        "commit": "This command is to commit the changes",
        "editable": "This command is to make the submodule editable in the git repository",
    }

    for key, value in help_list.items():
        print (Fore.GREEN + key + Style.RESET_ALL + " : " + value)