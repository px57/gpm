from git import Repo

class GitRepository(object):
    """
        @description: 
    """

    def __init__(
        self, 
        path: str, 
        **kwargs: dict
    ) -> None:
        """
            @description: 
            @params.path -> 
            @params.kwargs -> Faire passer l'ensemble des elements de configuration par ici.
            @params.kwargs.init_if_notexits(TODO) -> Permet d'indiquer s'il faut genere un nouveaux depot 
        """
        self.path = path
        self.init_if_notexits = kwargs.get('init_if_notexits', False) 

    def repository_exists(self, path: str) -> bool:
        """
            @description: 
        """
        return True

    def raiseerror_if_repository_dont_exists(self, path):
        """
            @description: 
        """
        if not self.repository_exists(path):
            raise Exception('Repository dont exists in ' + path)

    def get_change(self, **kwards):
        """
            @description: 
        """


    def __str__(self) -> str:
        """
            @desription: 
        """
        return 'GitRepository<' + self.path + '>'