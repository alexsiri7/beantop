class MockTelnet:
    def __init__(self):
        self.openCalled=False
        
    def open(self, host, port):
        self.openCalled=True
        
    def write(self,  message):
        self.lastMessage=message
        
    def read_until(self,  chars):
        if self.lastMessage == 'stats\r\n':
            return    ("current-jobs-ready: 5\n"
                         "pid: 1223\n"
                         "current-waiting: 12\n"
                         "current-workers: 4\n")
        elif self.lastMessage == 'list-tubes\r\n':
            return    ("data:\n")
        elif self.lastMessage == 'stats-tube data\r\n':
            return    ("current-jobs-delayed: 4\n"
                         "current-jobs-ready: 10\n"
                         "current-waiting: 6\n"
                         "current-watching: 12\n"
                         "current-jobs-reserved: 3\n")
        else:
            raise Exception("Unknown message: "+repr(self.lastMessage))

class MockOs:
    O_NONBLOCK=True
    def system(self,  message):
        pass
    
class MockFile():
    def __init__(self):
        self.char=None
        self.written=[]
        
    def fileno(self):
        return 1
        
    def read(self,  a):
        if self.char is None:
            raise IOError
        return self.char        
        
    def write(self, str):
        self.written.append(str)        
    
class MockSys:
    def __init__(self, file):
        self.stdin=file
        self.stdout =file
    
class MockTermios:
    ICANON=False
    ECHO=False
    TCSANOW=False
    TCSAFLUSH=True
    def tcgetattr(self, a):
        return [1, 2, 3, 4]
    def tcsetattr(self, a, b, c):
        pass
    
class MockFcntl:
    F_GETFL=True
    F_SETFL=True
    def fcntl(self, a, b, c=True):
        return True
        
        
class MockTime:
    def strftime(self, format, t):
        return 'timestring'
    def gmtime(self):
        return (1234, 123, 1234)
    def sleep(self,  secs):
        self.sleepSecs=secs
    def time(self):
        return 1234

class MockScreen:
    printcalls=0
    def render_screen(self):
        self.printcalls+=1
        return [""]

class MockIO:
    totalsleep=0
    def put_char(self, ch):
        self.ch=ch
    def get_char(self):
        if len(self.ch)>0:
            ch = self.ch[0]
            self.ch = self.ch[1:]
            return ch
        else:
            return None
    def gmtime(self):
        return self.totalsleep
    def get_printable_time(self):
        return ""
    def clear(self):
        pass
    def print_lines(self,  lines):
        pass
    def sleep(self,  seconds):
        self.totalsleep+=1
        pass
    def setup_terminal_for_char_read(self):
        pass
    def reset_terminal_options(self):
        pass

    
