import os, time, sys, termios, fcntl

class SysIO:
    clear = lambda c: os.system('clear')
    
    def getch(self):
      fd = sys.stdin.fileno()
      oldterm = termios.tcgetattr(fd)
      newattr = termios.tcgetattr(fd)
      newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
      termios.tcsetattr(fd, termios.TCSANOW, newattr)
      oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
      try:                 
          try:
            c = sys.stdin.read(1)
          except IOError: 
            c = None
      finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        pass
      return c
      
    def time(self):
        return time.time()
        
    def sleep(self, secs):
        return time.sleep(secs)
        
    def getTime(self):
        return time.strftime("%a, %d %b %Y %X", time.gmtime())
        
    def printlines(self, lines):
        for l in lines:
            print l
