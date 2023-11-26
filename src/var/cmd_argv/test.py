

from var import CommandLineParser
import unittest
import os

class TestCommandLineParser(unittest.TestCase):
    """
        @description: 
    """

    def test_spacename_unique(self):
        """
            @description: 
        """
        cmdline = CommandLineParser([
            'var.py', 
            'namespace', 
            'namespace2',
            '-p', 
            './aouaoeu', 
            '--salope', 
            'lol', 
            '--connasse="aoeuaeou"'
        ])
        self.assertEqual(cmdline.spacename, ['namespace', 'namespace2'])
        self.assertEqual(cmdline.arguments, [
            {'key': 'p', 'args': ['./aouaoeu']}, 
            {'key': 'salope', 'args': ['lol']}, 
            {'key': 'connasse', 'args': ['aoeuaeou']}
        ])
        # print (cmdline.spacename)
        # print (cmdline.arguments)


def run_cmd(argv: str):
    """
        @description: 
    """
    print ('python3 var.py ' + argv)
    os.system('python3 var.py ' + argv)
    
class TestCommandLine(unittest.TestCase):
    """
        @description: 

    """ 

    def test_withnamespace_only(self):
        """
            @description: 
        """
        run_cmd('namespace')

    def test_witharguments(self):
        """
            @description: 
        """
        run_cmd('namespace -p ./aouaoeu')

unittest.main()