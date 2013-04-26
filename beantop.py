#!/usr/bin/python
import telnetlib, yaml
import sys, getopt,os,time,string,termios,fcntl


class Bean:
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

   def stats(self):
      return self.format(self.yaml_data("stats", ["current-jobs-ready", "current-waiting", "current-workers"]))
   def tubestats(self):
      tubes = self.yaml_data("list-tubes", None)
      t_data = ""
      fields = ["current-jobs-delayed", "current-jobs-ready", 
		"current-jobs-reserved", "current-waiting"]
      ts = dict()
      header_width = 25
      field_width = 15
      max_items = 5
      for t in tubes:
          d = self.yaml_data("stats-tube "+t, 
		fields)
          if (d["current-jobs-delayed"]+d["current-jobs-reserved"]+d["current-jobs-ready"]>0):
            ts[t]=d
      rest = ts
      while len(rest)>0:
	      ts = dict(rest.items()[:max_items])
	      rest = dict(rest.items()[max_items:])
	      t_data += string.ljust("Tube", header_width)
	      for t,d in ts.iteritems(): 
		  t_data += string.ljust(t, field_width)
	      t_data +="\n"
	      for f in fields: 
		  t_data += string.rjust(f, header_width)
		  for t,d in ts.iteritems(): 
		    t_data += string.rjust(str(d[f]), field_width)
		  t_data +="\n"
      return t_data

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
   def format(self,dic):
      ret_data=""
      for k,v in dic.iteritems():
        ret_data+=k+": "+str(v)+"\n"
      return ret_data
   def printstatus(self):
      status = self.stats()
      tubestatus = self.tubestats()
      self.send("exit")
      clear()
      print time.strftime("%a, %d %b %Y %X", time.gmtime())     
      print status
      print tubestatus


clear = lambda: os.system('clear')
b = Bean()

def main(argv):
   try:
     opts, args = getopt.getopt(argv,"h:p:",[])
   except getopt.GetoptError:
      print argv[0],' -h <host> -p <port>'
      sys.exit(2)
   for opt,arg in opts:
     if opt=='-h':
        b.host = arg
     if opt=='-p':
	b.port = arg
   b.connect()
   mainloop()

def processCh():
   c = getch()
   p = False
   while c is not None:
     p = True
     if c=='q': 
       sys.exit()
     c = getch()
   return p     

def mainloop():
  while True:
    nt = time.time()+5
    b.printstatus()
    p = False
    while time.time()<nt and not p:
       p = processCh()
       time.sleep(0.1)




def getch():
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




if __name__ == "__main__":
   main(sys.argv[1:])
