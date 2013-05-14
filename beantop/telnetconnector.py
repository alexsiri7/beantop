
import telnetlib

class TelnetConnector:
   host = 'localhost'
   port = '11300'
   conn = None  
   def connect(self):
     self.conn = telnetlib.Telnet()
     self.conn.open(self.host, self.port)
   def send(self, mess):
      self.conn.write(mess+"\r\n")
   def readline(self):
      return self.conn.read_until("\n")
