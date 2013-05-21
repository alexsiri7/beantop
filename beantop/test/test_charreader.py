import unittest

from mocks import *
from beantop.charreader import CharReader
    
class Test(unittest.TestCase):
    def setUp(self):
        self.os=MockOs()
        self.file=MockFile()
        self.sys=MockSys(self.file)
        self.termios=MockTermios()
        self.fcntl=MockFcntl()
        self.char_reader = CharReader(self.os,  self.sys,  self.termios,  self.fcntl)

    def test_getchGetsNone(self):
        c = self.char_reader.get_char()
        self.assertEquals(None, c)

    def test_getchGetsException(self):
        c = self.char_reader.get_char()
        self.assertEquals(None, c)

    def test_getchGetsChar(self):
        self.file.char='a'
        c = self.char_reader.get_char()
        self.assertEquals('a', c)

    def test_setup_terminal_for_char_read(self):
        self.char_reader.setup_terminal_for_char_read()
        
    def test_reset_terminal_options(self):
        self.char_reader.reset_terminal_options()


if __name__ == "__main__":
    unittest.main() 
