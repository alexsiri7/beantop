import os, time, sys, termios, fcntl

class SysIO:
    clear = lambda c: os.system('clear')
       
    def getch(self):
        self._setupTerminalForCharRead()
        try:                 
          try:
            c = sys.stdin.read(1)
          except IOError: 
            c = None
        finally:
            self._setupTerminalForStandardUse()
        return c
      
    def time(self):
        return time.time()
        
    def sleep(self, secs):
        return time.sleep(secs)
        
    def getTime(self):
        return time.strftime("%a, %d %b %Y %X", time.gmtime())
        
    def printLines(self, lines):
        for line in lines:
            print line
            
    def _setupTerminalForCharRead(self):
      self.fd = sys.stdin.fileno()
      self.oldterm = termios.tcgetattr(self.fd)
      newattr = termios.tcgetattr(self.fd)
      newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
      termios.tcsetattr(self.fd, termios.TCSANOW, newattr)
      self.oldflags = fcntl.fcntl(self.fd, fcntl.F_GETFL)
      fcntl.fcntl(self.fd, fcntl.F_SETFL, self.oldflags | os.O_NONBLOCK)
    
    def _setupTerminalForStandardUse(self):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.oldterm)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.oldflags)
            
