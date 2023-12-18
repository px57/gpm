import sys
import re
import copy

def is_valid_variable_name(variable_name):
    # La regex permet de vérifier si la chaîne commence par une lettre ou un souligné,
    # suivie de lettres, chiffres ou soulignés subséquents.
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(regex_pattern, variable_name))

def delete_string_quote_if_exist(string: str):
    """
        @description: 
    """

class CommandLineParser(object):
    """
        @description: Ici ont donne en condition 
        le commande line et ont recoit un object qui permet de simplifier ca lecture. 
    """

    def __init__(self, argv: list):
        """
            @description:
            @params.arv(list<str>) ->   
        """
        self.argv = argv

    @property
    def spacename(self):
        """
            @description: Is the alphanumeric elements. 
        """
        spacename = []
        for argument in self.argv[1:]:
            if not self.is_spacename_argument(argument):
                return spacename
            spacename.append(argument)
        return spacename

    @property
    def arguments(self):
        """
            @description: get the argument and the arguments of arguments.
        """
        arguments = []
        argv = self.argv[len(self.spacename) + 1:]

        new_argument = {}
        for argument in argv:
            if self.is_letter_argument(argument):
                self.__append_newargs(new_argument, arguments)
                new_argument = {
                    'key': argument[1:],
                    'args': []
                }
                continue
            elif self.is_word_cmdargument(argument):
                self.__append_newargs(new_argument, arguments)
                new_argument = self.parse_wordargument(argument)
                continue

            new_argument['args'].append(argument)

        self.__append_newargs(new_argument, arguments)
        return arguments

    def __append_newargs(
        self, 
        new_argument: dict, 
        arguments: list
    ):
        """
            @description:
            @params.new_argument -> 
            @params.arguments ->  
        """
        if new_argument == {}:
            return 
        arguments.append(new_argument)
        arguments = {}


    def is_letter_argument(self, argument: str) -> bool:
        """
            @description: Valide this format "-p"
        """
        if len(argument) != 2:
            return False
        if argument[0] != '-':
            return False
        return argument[1]

    def is_word_cmdargument(self, argument: str) -> bool:
        """
            @description: 
        """
        if argument[0:2] != '--':
            return False
        
        self.parse_wordargument(argument)
        return True

    def is_spacename_argument(self, argument: str) -> bool:
        """
            @description: is alphanumeric argument. 
        """
        return is_valid_variable_name(argument)

    def parse_wordargument(self, argument: str):
        """
            @description: 
        """
        spl_argument = argument[2:].split('=')
        name = spl_argument[0]
        equal_argument = []

        if len(spl_argument) == 2:
            equal_argument = [spl_argument[1][1:-1]]

        if not is_valid_variable_name(name):
            raise Exception('the ' + name +  ' word arguments is not valid !')
        
        return {
            'key': name,
            'args': equal_argument
        }
        

class CmdArgv(object):
    """
        @description: 
    """

    def __init__(self, namespaceList: dict) -> None:
        """
            @description: 
        """
        self.__namespacelist = namespaceList
        self.__argv = CommandLineParser(sys.argv)
        self.__selected_spacename = self.get_method_to_spacename(
            self.__argv, 
            self.__namespacelist
        )

    def get_method_to_spacename(
        self, 
        argv: CommandLineParser,
        namespacelist: dict,
    ): 
        """
            @description: Recupere la liste des methodes d'une namespace bien particuliers
            @params.argv(CommandLineParser) ->
            @params.namespacelist -> Le cumul des namespaces. 
        """ 
        level_namespacelist = copy.deepcopy(namespacelist)
        for name in argv.spacename:
            err = {
                'DONT_EXIST': name + " this spacename don't exist."
            }
            if type(level_namespacelist) is list:
                raise Exception(err['DONT_EXIST'])
            if name not in level_namespacelist:
                raise Exception(err['DONT_EXIST'])
            level_namespacelist = copy.deepcopy(level_namespacelist[name])

        if type(level_namespacelist) is dict:
            if '__init__' not in level_namespacelist:
                raise Exception("__init__ dont exist in this namespace.")
            return level_namespacelist['__init__']
        return level_namespacelist

    def __validate_structure(self):
        """
            @description: 
        """
    
    def get_spacename(self, args):
        """
            @description: 
        """

    def execute(self):
        """
            @description: 
        """
        print ('--------------- [execute] ---------------')


# -------------------------- [UNITEST]
if __name__ == '__main__':
    def fonction():
        """
            @description: 
        """

    CmdArgv({
        'namespace': [
            {
                'keyname': 'help',
                'description': 'Usage of the function',
                'command': ['h', 'help'],
                'args': ['path', 'description'],
                'kwargs': [''],
                '__def__': fonction,
            },
        ],
        'new': {
            'module': [
                {
                    'description': 'Usage of the function',
                    'command': ['h', 'help'],
                    '__def__': fonction  
                }
            ]
        }
    }).execute()