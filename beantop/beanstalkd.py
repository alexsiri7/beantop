
import yaml
from telnetconnector import TelnetConnector

class Beanstalkd(TelnetConnector):
   def yaml_data(self, msg, fields):
      self.send(msg)
      self.readline()      
      self.readline()
      stats =  yaml.load(self.conn.read_until("\r\n"))
      if fields is None:
         return stats
      ret_data=dict()
      for d in fields:
        ret_data[d]=stats[d]
      return ret_data
