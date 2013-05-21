import unittest

from beantop.screenprinter import ScreenPrinter
from mock import *
   
class Test(unittest.TestCase):
    def setUp(self):
        self.os=Mock()
        self.file=Mock(write=MagicMock())
        self.sys=Mock(stdout=self.file)
        self.screen_printer = ScreenPrinter(self.os,  self.sys)
    
    def test_print_lines(self):
        lines = ['a', 'b']
        self.screen_printer.print_lines(lines)
        self.file.write.assert_has_calls([call('a\n'), call('b\n')])

    def test_clear(self):
        self.screen_printer.clear()
        self.assertTrue(self.os.wasClearCalled)
        self.os.clear.assert_called()
        


if __name__ == "__main__":
    unittest.main() 
