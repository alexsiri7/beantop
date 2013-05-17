
import telnetlib

HEADER_WIDTH = 25
FIELD_WIDTH = 15
GLOBAL_STATS_FIELDS = ["current-jobs-ready", "current-waiting", "current-workers"]
TUBE_STATS_FIELDS = ["current-jobs-delayed", "current-jobs-ready", "current-jobs-reserved", "current-waiting"]


class BeanstalkdStats:
    def __init__(self, beanstalkd):
        self.beanstalkd=beanstalkd
    def _stats(self):
        return self._format(
            self.beanstalkd.yaml_data_filtered("stats", GLOBAL_STATS_FIELDS))
        
    def _getTubes(self):
        return self.beanstalkd.yaml_data("list-tubes")
        
    def _getFilteredTubes(self):
        tubes = self._getTubes()
        ts = dict()
        for t in tubes:
            d = self.beanstalkd.yaml_data_filtered("stats-tube "+t, TUBE_STATS_FIELDS)
            if (d["current-jobs-delayed"]+d["current-jobs-reserved"]+d["current-jobs-ready"]>0):
                ts[t]=d
        return ts
        
    def _tubestats(self):
        ts = self._getFilteredTubes()
        t_data = []
        max_items = 5
        rest = ts
        while len(rest)>0:
            ts = dict(rest.items()[:max_items])
            rest = dict(rest.items()[max_items:])
            t_data += self._renderRow(ts)
        return t_data
        
    def _renderRow(self,  ts):
        t_data=[]
        t_headers = "Tube".ljust(HEADER_WIDTH)
        for t,d in ts.iteritems(): 
            t_headers += t.ljust(FIELD_WIDTH)
        t_data.append(t_headers)
        for f in TUBE_STATS_FIELDS: 
            t_row = f.rjust(HEADER_WIDTH)
            for t,d in ts.iteritems(): 
                t_row += str(d[f]).rjust(FIELD_WIDTH)
            t_data.append(t_row)
        return t_data

    def renderScreen(self):
      status = self._stats()
      tubestats = self._tubestats()
      return status+tubestats
      
    def _format(self,dic):
      ret_data=[]
      for k,v in dic.iteritems():
        ret_data.append(k+": "+str(v))
      return ret_data
