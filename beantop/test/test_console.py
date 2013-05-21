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
        
    def test_mainloop(self):
        self.char_reader.put_char(list("asdfr")+[None]*10+list("ffasq"))
        self.console.main_loop()
        self.assertEquals(11,  self.time.totalsleep)
        self.assertEquals(3,  self.screen.printcalls)

if __name__ == "__main__":
    unittest.main() 
