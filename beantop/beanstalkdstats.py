
HEADER_WIDTH = 25
FIELD_WIDTH = 15
GLOBAL_STATS_FIELDS = ["current-jobs-ready", 
                                "current-waiting", 
                                "pid",
                                "current-workers"]
TUBE_STATS_FIELDS = ["current-jobs-delayed", 
                            "current-jobs-ready", 
                            "current-jobs-reserved", 
                            "current-waiting", 
                            "current-watching"]


class BeanstalkdStats:
    def __init__(self, beanstalkd):
        self._beanstalkd = beanstalkd

    def render_screen(self):
        status = self._fetch_global_stats()
        tube_stats = self._fetch_tube_stats()
        return status+tube_stats
        
    def _fetch_global_stats(self):
        return self._format(
            self._beanstalkd.yaml_data_filtered("stats", GLOBAL_STATS_FIELDS))
    
    @staticmethod
    def _format(dic):
        ret_data = []
        for field, value in dic.iteritems():
            ret_data.append(field+": "+str(value))
        return ret_data        
                
    def _fetch_tube_stats(self):
        all_tubes = self._get_filtered_tubes()
        t_data = []
        max_items = 5
        remaining_tubes = all_tubes
        while len(remaining_tubes)>0:
            tubes_in_row = dict(remaining_tubes.items()[:max_items])
            remaining_tubes = dict(remaining_tubes.items()[max_items:])
            t_data += self._render_row(tubes_in_row)
        return t_data
        
    def _get_filtered_tubes(self):
        all_tubes = self._get_tubes()
        filtered_tubes = dict()
        for tube_name in all_tubes:
            tube = self._beanstalkd.yaml_data_filtered("stats-tube "+tube_name, 
                                                   TUBE_STATS_FIELDS)
            if (self._tube_has_meaningful_info(tube)):
                filtered_tubes[tube_name] = tube
        return filtered_tubes

    def _get_tubes(self):
        return self._beanstalkd.yaml_data("list-tubes")

    @staticmethod
    def _tube_has_meaningful_info(tube):
        return (tube["current-jobs-delayed"]+
                    tube["current-jobs-reserved"]+
                    tube["current-jobs-ready"])>0

    @staticmethod
    def _render_row(tubes_in_row):
        t_data = []
        t_headers = "Tube".ljust(HEADER_WIDTH)
        for tube_name, tube_data in tubes_in_row.iteritems(): 
            t_headers += tube_name.ljust(FIELD_WIDTH)
        t_data.append(t_headers)
        for field in TUBE_STATS_FIELDS: 
            t_row = field.rjust(HEADER_WIDTH)
            for tube_name, tube_data in tubes_in_row.iteritems(): 
                t_row += str(tube_data[field]).rjust(FIELD_WIDTH)
            t_data.append(t_row)
        return t_data

