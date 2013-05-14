import unittest

from beantop.console import Console

class MockScreen:
    pass

class MockIO:
    pass


class Test(unittest.TestCase):
    def setUp(self):
        self.sysio = MockScreen()
        self.screen = MockIO()
        self.console = Console(self.sysio)
        self.console.setScreen(self.screen)
        
    def test_connect_defaults(self):
        pass
    
if __name__ == "__main__":
    unittest.main() 
