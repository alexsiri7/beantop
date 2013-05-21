import unittest    

from mocks import *
from beantop.beanstalkdstats import BeanstalkdStats
from beantop.beanstalkd import Beanstalkd
from beantop.console import Console
from beantop.clock import Clock
from beantop.charreader import CharReader
from beantop.screenprinter import ScreenPrinter
from beantop.arguments import Arguments

class Test(unittest.TestCase):
    def setUp(self):
        self.mock_telnet = MockTelnet()
        self.mock_os = MockOs()
        self.mock_file=MockFile()        
        self.mock_file.char='q'
        self.mock_time = MockTime()        
        self.mock_sys = MockSys(self.mock_file)
        self.mock_termios = MockTermios()
        self.mock_fcntl = MockFcntl()
        
        self.beanstalkd = Beanstalkd(self.mock_telnet, '', '')
        self.stats = BeanstalkdStats(self.beanstalkd)
        self.char_reader = CharReader(self.mock_os, self.mock_sys, self.mock_termios, self.mock_fcntl)
        self.screen_printer = ScreenPrinter(self.mock_os, self.mock_sys)
        self.console = Console(Clock(self.mock_time),  self.char_reader,  self.screen_printer, self.stats)       

    def test_integration(self):
        self.beanstalkd.connect()
        self.console.main_loop()
    
if __name__ == "__main__":
    unittest.main() 
