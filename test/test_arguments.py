import unittest

from beantop.arguments import *

class MockFile:
    
    def __init__(self):
        self.written=[]
        
    def write(self, str):
        self.written.append(str)
        
class MockSys:
    def __init__(self):
        self.exitCalled=False
        self.stdout = MockFile()
        
    def exit(self, code):
        self.exitCalled=True

class MockGetOpt:
    GetoptError=Exception
    def __init__(self):
        self.returnParams=None
        
    def getopt(self, argv, options, longoptions):
        if self.returnParams is None:
            raise self.GetoptError()
        else:
            return (self.returnParams, [])

CUSTOM_PORT = 1234
CUSTOM_HOST='thehost'

class Test(unittest.TestCase):
    def setUp(self):
        self.sys=MockSys()
        self.getopt=MockGetOpt()
        self.arguments = Arguments(self.sys, self.getopt)
        
    def test_parseNoArguments(self):
        self.getopt.returnParams=[]

        host, port = self.arguments.process(['test'])
        
        self.assertEquals([],  self.sys.stdout.written)
        self.assertEquals(DEFAULT_HOST, host)
        self.assertEquals(DEFAULT_PORT, port)
        self.assertFalse(self.sys.exitCalled)

    def test_parseIncompleteArguments(self):
        self.getopt.returnParams=None  
        
        host, port = self.arguments.process(['test'])
        
        self.assertEquals(['test -h <host> -p <port>'],  self.sys.stdout.written)
        self.assertTrue(self.sys.exitCalled)
        
    def test_parseOnlyPort(self):
        self.getopt.returnParams=[('-p', CUSTOM_PORT)]
        
        host, port = self.arguments.process(['test'])
        
        self.assertEquals([],  self.sys.stdout.written)
        self.assertEquals(DEFAULT_HOST, host)
        self.assertEquals(CUSTOM_PORT, port)
        self.assertFalse(self.sys.exitCalled)
    
    def test_parseOnlyHost(self):
        self.getopt.returnParams=[('-h', CUSTOM_HOST)]
        
        host, port = self.arguments.process(['test'])
        
        self.assertEquals([],  self.sys.stdout.written)
        self.assertEquals(CUSTOM_HOST, host)
        self.assertEquals(DEFAULT_PORT, port)
        self.assertFalse(self.sys.exitCalled)
    
    def test_parseAllArguments(self):
        self.getopt.returnParams=[('-h', CUSTOM_HOST),('-p', CUSTOM_PORT)]
        
        host, port = self.arguments.process(['test'])
        
        self.assertEquals([],  self.sys.stdout.written)
        self.assertEquals(CUSTOM_HOST, host)
        self.assertEquals(CUSTOM_PORT, port)
        self.assertFalse(self.sys.exitCalled)

if __name__ == "__main__":
    unittest.main() 
