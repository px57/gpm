
class Version(object):
    """
        @description: 
    """

    def __init__(self, version: str): 
        """
            @description: 
        """
        self.version = version
        self.__parsed_version = self.__parse_string_value(version)

    def __parse_string_value(self, version: str):
        """
            @description: parse 1.22.234 (main) to 
                {
                    'num': '1.22.234',
                    'branch': 'main',
                }
        """
        spl_version = version.split(' ')
        return {
            'num': spl_version[0],
            'branch': spl_version[1][1:-1]
        }

    @property
    def branch(self):
        """
            @description: 
        """
        return self.__parsed_version['branch']
    
    @property
    def num(self):
        """
            @description: 
        """
        return self.__parsed_version['num']
    
    @property
    def integer_list_version(self):
        """
            @description: Convertir  1.11.110 en [1, 11, 110] pour pouvoir travailler sur la data.
        """
        integer_version = [int(a) for a in self.num.split('.')]
        return integer_version

    def convert_integer_list_to_str(self, integer_list: list):
        """
            @description: Convertir integer_list_version en version.
        """
        str_list = [str(a) for a in integer_list]
        return '.'.join(str_list)

    @property
    def next_number(self):
        """
            @description: Generer le nombre d'apres  
        """
        integer_list_version = self.integer_list_version
        if integer_list_version[2] != 999:
            integer_list_version[2] += 1
            return self.convert_integer_list_to_str(integer_list_version)
        
        integer_list_version[2] = 0
        if integer_list_version[1] != 99:
            integer_list_version[1] += 1
            return self.convert_integer_list_to_str(integer_list_version)
    
        integer_list_version[1] = 0
        integer_list_version[0] += 1
        return self.convert_integer_list_to_str(integer_list_version)

    def next(self):
        """
            @description: Avancer vers la version suivante. 
            1.11.110                                                                                                                                                                                                                                                                                                                  
        """
        next_number = self.next_number
        self.__parsed_version['num'] = next_number