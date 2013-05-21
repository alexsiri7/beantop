
class ScreenPrinter:    
    def __init__(self,  operative_system,  sys):
        self._operative_system = operative_system
        self._sys = sys
                  
    def print_lines(self, lines):
        for line in lines:
            self._sys.stdout.write(line+'\n')
    
    def clear(self):
        self._operative_system.system('clear')
