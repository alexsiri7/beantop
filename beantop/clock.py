
class Clock:
    def __init__(self,  time_library):
        self._time_library = time_library
    
    def gmtime(self):
        return self._time_library.time()
        
    def sleep(self, secs):
        return self._time_library.sleep(secs)
        
    def get_printable_time(self):
        return self._time_library.strftime("%a, %d %b %Y %X", 
                                          self._time_library.gmtime())
