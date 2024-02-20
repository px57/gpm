
from kernel.modules.migrations_expurge import migration_expurge 

def commandline__expurge_makemigrations():
    """
    This function is to delete all the migrations files.
    """
    migration_expurge()
    print ("expurge_makemigrations done.")
