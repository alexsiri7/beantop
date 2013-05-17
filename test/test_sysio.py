import unittest

from beantop.sysio import SysIO

class MockOs:
    O_NONBLOCK=True
    pass

class MockTime:
    def strftime(self, format, t):
        return 'timestring'
    def gmtime(self):
        return 1234
    def sleep(self,  secs):
        self.sleepSecs=secs

    
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
    
class MockTermios:
    ICANON=False
    ECHO=False
    TCSANOW=False
    TCSAFLUSH=True
    def tcgetattr(self, a):
        return [1, 2, 3, 4]
    def tcsetattr(self, a, b, c):
        pass
    
class MockFcntl:
    F_GETFL=True
    F_SETFL=True
    def fcntl(self, a, b, c=True):
        return True
    
class Test(unittest.TestCase):
    def setUp(self):
        self.os=MockOs()
        self.time=MockTime()
        self.file=MockFile()
        self.sys=MockSys(self.file)
        self.termios=MockTermios()
        self.fcntl=MockFcntl()
        self.sysio = SysIO(self.os,  self.time,  self.sys,  self.termios,  self.fcntl)

    def test_getchGetsNone(self):
        c = self.sysio.getch()
        self.assertEquals(None, c)

    def test_getchGetsException(self):
        c = self.sysio.getch()
        self.assertEquals(None, c)


    def test_getchGetsChar(self):
        self.file.char='a'
        c = self.sysio.getch()
        self.assertEquals('a', c)

    def test_getTime(self):
        t = self.sysio.getTime()
        self.assertEquals('timestring', t)
        
    def test_gmtime(self):
        t = self.sysio.gmtime()
        self.assertEquals(1234, t)

    def test_sleep(self):
        self.sysio.sleep(10)
        self.assertTrue(10,  self.time.sleepSecs)
    
    def test_printLines(self):
        lines = ['a', 'b']
        self.sysio.printLines(lines)
        self.assertEquals(['a\n', 'b\n'],  self.file.written)

if __name__ == "__main__":
    unittest.main() 
