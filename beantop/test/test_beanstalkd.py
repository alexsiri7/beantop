import unittest

from beantop.beanstalkd import Beanstalkd
from mocks import MockTelnet

class Test(unittest.TestCase):
    def setUp(self):
        self.telnet = MockTelnet()
        self.beanstalkd = Beanstalkd(self.telnet, 'thehost', 9057)
                        
    def test_connect(self):
        self.beanstalkd.connect()
        self.assertTrue(self.telnet.openCalled)        
        
    def test_yaml_data(self):
        line = self.beanstalkd.yaml_data("stats")
        self.assertEquals({'current-jobs-ready': 5, 'current-waiting': 12, 'current-workers': 4,  'pid':1223}, line)
        
    def test_yaml_data_filtered(self):
        line = self.beanstalkd.yaml_data_filtered("stats",  ["current-jobs-ready",  "current-waiting"])
        self.assertEquals({'current-jobs-ready': 5, 'current-waiting': 12}, line)

if __name__ == "__main__":
    unittest.main() 
