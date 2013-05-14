import os, time, sys, termios, fcntl

class Console:
    clear = lambda c: os.system('clear')
    def setScreen(self, s):
        self.screen=s
    def processCh(self):
       c = self.getch()
       p = False
       while c is not None:
         p = True
         if c=='q': 
           sys.exit()
         c = self.getch()
       return p     

    def mainloop(self):
      while True:
        nt = time.time()+5
        scr = self.screen.renderScreen()
        self.clear()
        print time.strftime("%a, %d %b %Y %X", time.gmtime())
        for s in scr:
            print s
        p = False
        while time.time()<nt and not p:
           p = self.processCh()
           time.sleep(0.1)

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
          except IOError: c = None
      finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
      return c
    
