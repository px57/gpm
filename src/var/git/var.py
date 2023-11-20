from libs import convert_time_string_to_datetime

import git
import os
import json
import pprint

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
        self.repo = git.Repo(self.path)
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

    def get_diff_files(self, sha1):
        """
            @description: Get diff in json format 
        """
        diff = self.repo.git.diff(sha1, name_only=True)
        return diff.split('\n')

    def get_files_change(self, **kwargs):
        """
            @description: Get all change in repository 
        """
        commit_list = self.commit_list()
        files_change = {}
        for commit in commit_list:
            sha1 = commit['commit']
            files_change[sha1] = self.get_diff_files(commit['commit'])
        return files_change

    def commit_list(self, **kwargs):
        """
            @description:
            git log --pretty=format:'{ "commit": "%H", "author": "%an <%ae>", "date": "%ad", "message": "%s", "changes": [ %n%b ] }' 
        """
        commit_log = self.repo.git.log(
            '--pretty=format:{ "commit": "%H", "author": "%an <%ae>", "date": "%ad", "message": "%s" }', 
            '--all', 
            '--decorate'
        ).split('\n')
        commit_list = []
        for commit in commit_log:
            json_dict = json.loads(commit)
            json_dict['date'] = convert_time_string_to_datetime(json_dict['date'])
            commit_list.append(json_dict)

        return commit_list
    
    def __str__(self) -> str:
        """
            @desription: 
        """
        return 'GitRepository<' + self.path + '>'