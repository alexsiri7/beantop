class Console:
    def __init__(self,  sysio,  screen):
        self.sysio=sysio
        self.screen=screen
        self.finished=False
        
    def setScreen(self, s):
        self.screen=s
        
    def processChar(self):
        c = self.sysio.getch()
        if c is None:
            return False
        if c=='q': 
            self.finished=True
        return True
       
    def processCharQueue(self):
       foundChar = self.processChar()
       while foundChar and not self.finished:
            foundChar = self.processChar()
       

    def runlooponce(self):
        nt = self.sysio.time()+5
        scr = self.screen.renderScreen()
        self.sysio.clear()
        time = self.sysio.getTime()
        self.sysio.printLines([time]+scr)
        p = False
        while self.sysio.time()<nt and not self.finished:
           self.processCharQueue()
           self.sysio.sleep(0.1)
           
    def mainloop(self):
      while not self.finished:
        self.runlooponce()
