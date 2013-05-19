import unittest

from beantop.sysio import ScreenPrinter

class MockOs:
    O_NONBLOCK=True
    def __init__(self,  ):
        self.wasClearCalled=False
        
    def system(self,  method):
        if method=='clear':
            self.wasClearCalled=True

class MockFile():
    def __init__(self):
        self.char=None
        self.written=[]
        
    def fileno(self):
        return 1
        
    def read(self,  a):
        if self.char is None:
            raise IOError
        return self.char        
        
    def write(self, str):
        self.written.append(str)        
    
class MockSys:
    def __init__(self, file):
        self.stdin=file
        self.stdout =file
    
class Test(unittest.TestCase):
    def setUp(self):
        self.os=MockOs()
        self.file=MockFile()
        self.sys=MockSys(self.file)
        self.screen_printer = ScreenPrinter(self.os,  self.sys)
    
    def test_print_lines(self):
        lines = ['a', 'b']
        self.screen_printer.print_lines(lines)
        self.assertEquals(['a\n', 'b\n'],  self.file.written)

    def test_clear(self):
        self.screen_printer.clear()
        self.assertTrue(self.os.wasClearCalled)


if __name__ == "__main__":
    unittest.main() 
