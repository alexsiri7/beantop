import unittest

from beantop.arguments import *
from mock import *

CUSTOM_PORT = 1234
CUSTOM_HOST='thehost'

class MockError(Exception):
    pass

class Test(unittest.TestCase):
    def setUp(self):
        self.sys=Mock(stdout=MagicMock())
        self.opts=MagicMock()
        self.getopt=Mock(getopt=self.opts, GetoptError=MockError)
        self.arguments = Arguments(self.sys, self.getopt)
        
    def test_parseNoArguments(self):
        self.opts.return_value=[], None

        connection_params = self.arguments.process(['test'])
        
        self.assertOutput([])
        self.assertEquals((DEFAULT_HOST, DEFAULT_PORT),  connection_params)        
        self.assertNotAppClosed()

    def test_parseIncompleteArguments(self):
        self.opts.side_effect=MockError
        
        connection_params = self.arguments.process(['test'])
        
        self.assertOutput(['test -h <host> -p <port>'])
        self.assertAppClosed()
        
    def test_parseOnlyPort(self):
        self.opts.return_value=[('-p', CUSTOM_PORT)], None
        
        connection_params = self.arguments.process(['test'])
        
        self.assertOutput([])
        self.assertEquals((DEFAULT_HOST, CUSTOM_PORT),  connection_params)        
        self.assertNotAppClosed()
    
    def test_parseOnlyHost(self):
        self.opts.return_value=[('-h', CUSTOM_HOST)], None
        
        connection_params = self.arguments.process(['test'])
        
        self.assertOutput([])
        self.assertEquals((CUSTOM_HOST, DEFAULT_PORT),  connection_params)
        self.assertNotAppClosed()
    
    def test_parseAllArguments(self):
        self.opts.return_value=[('-h', CUSTOM_HOST),('-p', CUSTOM_PORT)], None
        
        connection_params = self.arguments.process(['test'])
        
        self.assertOutput([])
        self.assertEquals((CUSTOM_HOST, CUSTOM_PORT),  connection_params)
        self.assertNotAppClosed()
        
    def assertAppClosed(self):
        self.assertAppClosedIs(True)
    
    def assertNotAppClosed(self):
        self.assertAppClosedIs(False)
    
    def assertAppClosedIs(self, state):
        self.sys.exit.assert_was_called(state)
        
    def assertOutput(self, lines):
        calls = map(call,  lines)
        self.sys.stdout.write.assert_has_calls(calls)

if __name__ == "__main__":
    unittest.main() 
