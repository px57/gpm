

from colorama import Fore, Style, init

def raise_error(message: str = None):
    """
    Raise an error.
    """
    raise Exception(Fore.RED + ">>> Error: " + message + Style.RESET_ALL)