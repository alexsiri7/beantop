import unittest

from beantop.beanstalkd import Beanstalkd

class MockTelnet:
    def __init__(self):
        self.openCalled=False
        
    def open(self, host, port):
        self.openCalled=True
        
    def write(self,  message):
        self.lastMessage=message
        
    def read_until(self,  chars):
        return    ("data:\n"
                     "field_1: a value\n"
                     "field_2: other value\n")


class Test(unittest.TestCase):
    def setUp(self):
        self.telnet = MockTelnet()
        self.beanstalkd = Beanstalkd(self.telnet, 'thehost', 9057)
                        
    def test_send(self):
        self.beanstalkd.send("amessage")
        self.assertEquals("amessage\r\n", self.telnet.lastMessage)

    def test_connect(self):
        self.beanstalkd.connect()
        self.assertTrue(self.telnet.openCalled)        


    def test_readline(self):
        line = self.beanstalkd.readline()
        self.assertEquals("data:\nfield_1: a value\nfield_2: other value\n", line)
        
    def test_yaml_data(self):
        line = self.beanstalkd.yaml_data("amessage")
        self.assertEquals({'data':None,'field_1':'a value', 'field_2':'other value'}, line)
        
    def test_yaml_data_filtered(self):
        line = self.beanstalkd.yaml_data_filtered("amessage",  ["field_1",  "field_2"])
        self.assertEquals({'field_1':'a value', 'field_2':'other value'}, line)

if __name__ == "__main__":
    unittest.main() 
