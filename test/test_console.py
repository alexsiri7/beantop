import unittest

from beantop.console import Console

class MockScreen:
    printcalls=0
    def renderScreen(self):
        self.printcalls+=1
        return [""]

class MockIO:
    totalsleep=0
    def putchar(self, ch):
        self.ch=ch
    def getch(self):
        if len(self.ch)>0:
            ch = self.ch[0]
            self.ch = self.ch[1:]
            return ch
        else:
            return None
    def time(self):
        return self.totalsleep
    def getTime(self):
        return ""
    def clear(self):
        pass
    def printLines(self,  lines):
        pass
    def sleep(self,  seconds):
        self.totalsleep+=1
        pass



class Test(unittest.TestCase):
    def setUp(self):
        self.screen = MockScreen()
        self.sysio = MockIO()
        self.console = Console(self.sysio)
        self.console.setScreen(self.screen)
        
    def test_process_char_None(self):
        self.sysio.putchar("")
        res = self.console.processChar()
        self.assertEquals(False,  res)
        self.assertEquals(False,  self.console.finished)
    
    def test_process_char_Other(self):
        self.sysio.putchar('a')
        res = self.console.processChar()
        self.assertEquals(True,  res)
        self.assertEquals(False,  self.console.finished)
    
    def test_process_char_q(self):
        self.sysio.putchar('q')
        res = self.console.processChar()
        self.assertEquals(True,  res)
        self.assertEquals(True,  self.console.finished)
    
    def test_process_char_queue(self):
        self.sysio.putchar('asdfqasdf')
        self.console.processCharQueue()
        self.assertEquals(True,  self.console.finished)

    def test_process_char_queue(self):
        self.sysio.putchar('asdfa')
        self.console.processCharQueue()
        self.assertEquals(False,  self.console.finished)

    def test_mainloop(self):
        self.sysio.putchar(list("asdfa")+[None]*10+list("ffasq"))
        self.console.mainloop()
        self.assertEquals(True,  self.console.finished)
        self.assertEquals(11,  self.sysio.totalsleep)
        self.assertEquals(3,  self.screen.printcalls)

if __name__ == "__main__":
    unittest.main() 
