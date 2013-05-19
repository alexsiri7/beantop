import unittest

from beantop.factory import *

class Test(unittest.TestCase):
    def test_create_arguments_parser(self):
        create_arguments_parser()
    def test_start_application(self):
        start_application('', '')

    
if __name__ == "__main__":
    unittest.main() 
