import unittest

from beantop.beanstalkd import Beanstalkd
from mocks import MockTelnet

class Test(unittest.TestCase):
    def setUp(self):
        self.telnet = MockTelnet()
        self.beanstalkd = Beanstalkd(self.telnet, 'thehost', 9057)
                        
    def test_send(self):
        self.beanstalkd.send("stats")
        self.assertEquals("stats\r\n", self.telnet.lastMessage)

    def test_connect(self):
        self.beanstalkd.connect()
        self.assertTrue(self.telnet.openCalled)        

    def test_readline(self):
        self.beanstalkd.send("stats")        
        line = self.beanstalkd.readline()
        self.assertEquals("current-jobs-ready: 5\ncurrent-waiting: 12\ncurrent-workers: 4\n", line)
        
    def test_yaml_data(self):
        line = self.beanstalkd.yaml_data("stats")
        self.assertEquals({'current-jobs-ready': 5, 'current-waiting': 12, 'current-workers': 4}, line)
        
    def test_yaml_data_filtered(self):
        line = self.beanstalkd.yaml_data_filtered("stats",  ["current-jobs-ready",  "current-waiting"])
        self.assertEquals({'current-jobs-ready': 5, 'current-waiting': 12}, line)

if __name__ == "__main__":
    unittest.main() 
