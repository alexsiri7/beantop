
import telnetlib

class BeanstalkdStats:
    GLOBAL_STATS_FIELDS = ["current-jobs-ready", "current-waiting", "current-workers"]
    TUBE_STATS_FIELDS = ["current-jobs-delayed", "current-jobs-ready", "current-jobs-reserved", "current-waiting"]
    def __init__(self, b):
        self.b=b
    def stats(self):
        return self.format(self.b.yaml_data_filtered("stats", self.GLOBAL_STATS_FIELDS))
        
    def _getTubes(self):
        return self.b.yaml_data("list-tubes")
        
    def tubestats(self):
        tubes = self._getTubes()
        t_data = ""
        ts = dict()
        for t in tubes:
            d = self.b.yaml_data_filtered("stats-tube "+t, self.TUBE_STATS_FIELDS)
            if (d["current-jobs-delayed"]+d["current-jobs-reserved"]+d["current-jobs-ready"]>0):
                ts[t]=d
        max_items = 5
            
        rest = ts
        while len(rest)>0:
            ts = dict(rest.items()[:max_items])
            rest = dict(rest.items()[max_items:])
            t_data += self.renderRow(ts)
        return t_data
    def renderRow(self,  ts):
        header_width = 25
        field_width = 15
        t_data = "Tube".ljust(header_width)
        for t,d in ts.iteritems(): 
            t_data += t.ljust(field_width)
        t_data +="\n"
        for f in self.TUBE_STATS_FIELDS: 
            t_data += f.rjust(header_width)
            for t,d in ts.iteritems(): 
                t_data += str(d[f]).rjust(field_width)
            t_data +="\n"
        return t_data

    def renderScreen(self):
      status = self.stats()
      tubestatus = self.tubestats()
      return [status, tubestatus]
    def format(self,dic):
      ret_data=""
      for k,v in dic.iteritems():
        ret_data+=k+": "+str(v)+"\n"
      return ret_data
