import unittest

from beantop.beanstalkdstats import BeanstalkdStats

class MockBeanstalkd:
    printcalls=0
    def yaml_data(self,  message):
        return ["tube_1",  "tube_2"]
    def yaml_data_filtered(self,  message,  fields):
        if message=="stats":
            return {"current-jobs-ready":1, "current-waiting":2, "current-workers":3}
        else:
            return {"current-jobs-delayed":1, 
                        "current-jobs-reserved":2, 
                        "current-jobs-ready":3, 
                        "current-waiting":12}


class Test(unittest.TestCase):
    def setUp(self):
        self.beanstalkd=MockBeanstalkd()
        self.beanstalkdstats = BeanstalkdStats(self.beanstalkd)
        
    def test_stats(self):
        stats=self.beanstalkdstats._stats()
        self.assertEquals("current-jobs-ready: 1\ncurrent-waiting: 2\ncurrent-workers: 3\n", stats)
        
    def test_tubestats(self):
        stats=self.beanstalkdstats._tubestats()
        self.assertEquals("Tube                     tube_1         tube_2         \n     current-jobs-delayed              1              1\n       current-jobs-ready              3              3\n    current-jobs-reserved              2              2\n          current-waiting             12             12\n", stats)

if __name__ == "__main__":
    unittest.main() 
