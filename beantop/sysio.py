import os, time, sys, termios, fcntl

class SysIO:
    clear = lambda c: os.system('clear')
       
    def getch(self):
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
      fd = sys.stdin.fileno()
      self.oldterm = termios.tcgetattr(fd)
      newattr = termios.tcgetattr(fd)
      newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
      termios.tcsetattr(fd, termios.TCSANOW, newattr)
      self.oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
    def _setupTerminalForStandardUse(self):
        termios.tcsetattr(fd, termios.TCSAFLUSH, self.oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, self.oldflags)
            
