import unittest

from mocks import *
from beantop.clock import Clock
    
class Test(unittest.TestCase):
    def setUp(self):
        self.mock_time = MockTime()
        self.time = Clock(self.mock_time)

    def test_get_printable_time(self):
        t = self.time.get_printable_time()
        self.assertEquals('timestring', t)
        
    def test_gmtime(self):
        t = self.time.gmtime()
        self.assertEquals(1234, t)

    def test_sleep(self):
        self.time.sleep(10)
        self.assertTrue(10,  self.mock_time.sleepSecs)
    
if __name__ == "__main__":
    unittest.main() 
