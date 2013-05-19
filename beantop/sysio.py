
class Time:
    def __init__(self,  time_library):
        self.time_library = time_library
    
    def gmtime(self):
        return self.time_library.time()
        
    def sleep(self, secs):
        return self.time_library.sleep(secs)
        
    def get_printable_time(self):
        return self.time_library.strftime("%a, %d %b %Y %X", 
                                          self.time_library.gmtime())

class CharReader:
       
    def __init__(self,  operative_system, sys, termios, fcntl):
        self.operative_system = operative_system
        self.sys = sys
        self.termios = termios
        self.fcntl = fcntl
        self.stdin_file_descriptor = None
        self.oldterm = None
        self.oldflags = None
    
    def get_char(self):
        try:
            char_read = self.sys.stdin.read(1)
        except IOError: 
            char_read = None
        return char_read

    def setup_terminal_for_char_read(self):
        self.stdin_file_descriptor = self.sys.stdin.fileno()
        self.oldterm = self.termios.tcgetattr(self.stdin_file_descriptor)
        newattr = self.termios.tcgetattr(self.stdin_file_descriptor)
        newattr[3] = newattr[3] & ~self.termios.ICANON & ~self.termios.ECHO
        self.termios.tcsetattr(self.stdin_file_descriptor
                               , self.termios.TCSANOW, newattr)
        self.oldflags = self.fcntl.fcntl(self.stdin_file_descriptor
                                         , self.fcntl.F_GETFL)
        newflags = self.oldflags | self.operative_system.O_NONBLOCK
        self.fcntl.fcntl(self.stdin_file_descriptor
                         , self.fcntl.F_SETFL, newflags)
    
    def reset_terminal_options(self):
        self.termios.tcsetattr(self.stdin_file_descriptor
                               , self.termios.TCSAFLUSH, self.oldterm)
        self.fcntl.fcntl(self.stdin_file_descriptor
                         , self.fcntl.F_SETFL, self.oldflags)    

class ScreenPrinter:    
    def __init__(self,  operative_system,  sys):
        self.operative_system = operative_system
        self.sys = sys
                  
    def print_lines(self, lines):
        for line in lines:
            self.sys.stdout.write(line+'\n')
    
    def clear(self):
        self.operative_system.system('clear')
