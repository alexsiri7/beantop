import unittest

from beantop.beanstalkdstats import BeanstalkdStats

class MockBeanstalkd:
    printcalls=0
    def yaml_data(self,  message):
        return ["tube_1",  "tube_2"]
    def yaml_data_filtered(self,  message,  fields):
        if message=="stats":
            return {"current-jobs-ready":1, "current-waiting":2, "current-workers":3, "pid": 1223}
        else:
            return {"current-jobs-delayed":1, 
                    "current-jobs-reserved":2, 
                    "current-jobs-ready":3, 
                    "current-waiting":12, 
                    "current-watching":32}


class Test(unittest.TestCase):
    def setUp(self):
        self.beanstalkd=MockBeanstalkd()
        self.beanstalkdstats = BeanstalkdStats(self.beanstalkd)
        
    def test_renderScreen(self):
        stats=self.beanstalkdstats.render_screen()
        self.assertEquals(
            ['current-jobs-ready: 1',
             'current-waiting: 2',
            'pid: 1223',             
             'current-workers: 3',
             'Tube                     tube_1         tube_2         ',
             '     current-jobs-delayed              1              1',
             '       current-jobs-ready              3              3',
             '    current-jobs-reserved              2              2',
             '          current-waiting             12             12', 
             '         current-watching             32             32'], stats)

if __name__ == "__main__":
    unittest.main() 
