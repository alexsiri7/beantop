class Console:
    def __init__(self,  sysio):
        self.sysio=sysio
        self.finished=False
        
    def setScreen(self, s):
        self.screen=s
        
    def processCh(self):
       c = self.sysio.getch()
       p = False
       while c is not None:
         p = True
         if c=='q': 
           self.finished=True
           return True
         c = self.sysio.getch()
       return p     

    def runlooponce(self):
        nt = self.sysio.time()+5
        scr = self.screen.renderScreen()
        self.sysio.clear()
        time = self.sysio.getTime()
        self.sysio.printlines([time]+scr)
        p = False
        while self.sysio.time()<nt and not p:
           p = self.processCh()
           self.sysio.sleep(0.1)
           
    def mainloop(self):
      while not self.finished:
        self.runlooponce()
