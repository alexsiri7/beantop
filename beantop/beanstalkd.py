
import yaml

class Beanstalkd:
    host = None
    port = None
    conn = None  
    def __init__(self,  conn,  host,  port):
        self.conn = conn       
        self.host=host
        self.port=port
     
    def connect(self):
        print "Connecting to", self.host, self.port
        self.conn.open(self.host, self.port)
    
    def send(self, mess):
        self.conn.write(mess+"\r\n")
      
    def readline(self):
        return self.conn.read_until("\n")    
      
    def yaml_data_filtered(self, msg, fields):
        stats =  self.yaml_data(msg)
        ret_data=dict()
        for d in fields:
            ret_data[d]=stats[d]
        return ret_data
        
    def yaml_data(self, msg):
        self.send(msg)
        self.readline()      
        self.readline()
        stats =  yaml.load(self.conn.read_until("\r\n"))
        return stats
