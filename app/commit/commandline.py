
import os 

def commandline__commit():
    """
    This function is to commit the changes.
    """
    os.system('git add -A')
    os.system('commitgpt --suggestions 7 --max-tokens 100 ""')
    # git add -A ; commitgpt --suggestions 7 --max-tokens 100 ""