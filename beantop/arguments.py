
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 11300

class Arguments:
    def __init__(self, system, getopt):
        self._system = system
        self._getopt = getopt
        
    def process(self, argv):
        try:
            opts, _ = self._getopt.getopt(argv, "h:p:", [])
        except self._getopt.GetoptError:
            self._system.stdout.write(argv[0]+' -h <host> -p <port>')
            self._system.exit(2)
            return None, None
        host = DEFAULT_HOST
        port = DEFAULT_PORT
        for opt, arg in opts:
            if opt == '-h':
                host = arg
            if opt == '-p':
                port = arg
        return host, port

