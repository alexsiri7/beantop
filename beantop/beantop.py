#!/usr/bin/env python
import sys, getopt
from factory import Factory

def main(argv):
    try:
        b, stats,  console=Factory.startApplication()
        opts, args = getopt.getopt(argv,"h:p:",[])
    except getopt.GetoptError:
        print argv[0],' -h <host> -p <port>'
        sys.exit(2)
    host = port = None
    for opt,arg in opts:
        if opt=='-h':
            host = arg
        if opt=='-p':
            port = arg
    b.connect(host, port)
    console.setScreen(stats)
    console.mainloop()


if __name__ == "__main__":
   main(sys.argv[1:])
