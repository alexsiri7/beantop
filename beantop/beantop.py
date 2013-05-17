#!/usr/bin/env python

from factory import Factory
import sys

def main(argv):
    arguments = Factory.createArgumentsParser()
    host, port = arguments.process(argv)
    b,  console=Factory.startApplication(host, port)
    b.connect()
    console.mainloop()


if __name__ == "__main__":
   main(sys.argv[1:])
