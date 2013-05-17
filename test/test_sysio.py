import unittest

from beantop.sysio import SysIO

class Test(unittest.TestCase):
    def setUp(self):
        self.sysio = SysIO()
    def test_none(self):
        pass

if __name__ == "__main__":
    unittest.main() 
