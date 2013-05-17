
class SysIO:
    clear = lambda c: os.system('clear')
       
    def __init__(self,  os, time, sys, termios, fcntl):
        self.os=os
        self.time=time
        self.sys=sys
        self.termios=termios
        self.fcntl=fcntl
    
    def getch(self):
        self._setupTerminalForCharRead()
        try:                 
          try:
            c = self.sys.stdin.read(1)
          except IOError: 
            c = None
        finally:
            self._setupTerminalForStandardUse()
        return c
      
    def gmtime(self):
        return self.time.gmtime()
        
    def sleep(self, secs):
        return self.time.sleep(secs)
        
    def getTime(self):
        return self.time.strftime("%a, %d %b %Y %X", self.gmtime())
        
    def printLines(self, lines):
        for line in lines:
            self.sys.stdout.write(line+'\n')
            
    def _setupTerminalForCharRead(self):
      self.fd = self.sys.stdin.fileno()
      self.oldterm = self.termios.tcgetattr(self.fd)
      newattr = self.termios.tcgetattr(self.fd)
      newattr[3] = newattr[3] & ~self.termios.ICANON & ~self.termios.ECHO
      self.termios.tcsetattr(self.fd, self.termios.TCSANOW, newattr)
      self.oldflags = self.fcntl.fcntl(self.fd, self.fcntl.F_GETFL)
      self.fcntl.fcntl(self.fd, self.fcntl.F_SETFL, self.oldflags | self.os.O_NONBLOCK)
    
    def _setupTerminalForStandardUse(self):
        self.termios.tcsetattr(self.fd, self.termios.TCSAFLUSH, self.oldterm)
        self.fcntl.fcntl(self.fd, self.fcntl.F_SETFL, self.oldflags)
            
