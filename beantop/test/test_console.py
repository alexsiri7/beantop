import unittest

from mocks import *
from beantop.console import Console

class Test(unittest.TestCase):
    def setUp(self):
        self.screen = MockScreen()
        self.time = MockIO()
        self.char_reader = MockIO()
        self.screen_printer = MockIO()
        self.console = Console(self.time, self.char_reader,  self.screen_printer, self.screen)
        
    def test_process_char_None(self):
        self.char_reader.put_char("")
        res = self.console._process_char()
        self.assertEquals(False,  res)
        self.assertEquals(False,  self.console.finished)
    
    def test_process_char_Other(self):
        self.char_reader.put_char('a')
        res = self.console._process_char()
        self.assertEquals(True,  res)
        self.assertEquals(False,  self.console.finished)
    
    def test_process_char_q(self):
        self.char_reader.put_char('q')
        res = self.console._process_char()
        self.assertEquals(True,  res)
        self.assertEquals(True,  self.console.finished)
    
    def test_process_char_queue_quit_and_write(self):
        self.char_reader.put_char('asdfqasdf')
        self.console._process_char_queue()
        self.assertEquals(True,  self.console.finished)
        self.assertEquals(4,  len(self.char_reader.ch))

    def test_process_char_queue_noquit(self):
        self.char_reader.put_char('asdfa')
        self.console._process_char_queue()
        self.assertEquals(False,  self.console.finished)
        self.assertEquals(0,  len(self.char_reader.ch))

    def test_mainloop(self):
        self.char_reader.put_char(list("asdfa")+[None]*10+list("ffasq"))
        self.console.main_loop()
        self.assertEquals(True,  self.console.finished)
        self.assertEquals(11,  self.time.totalsleep)
        self.assertEquals(3,  self.screen.printcalls)

if __name__ == "__main__":
    unittest.main() 
