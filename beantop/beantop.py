#!/usr/bin/env python

import factory 
import sys

def main(argv):
    arguments = factory.create_arguments_parser()
    host, port = arguments.process(argv)
    beanstalkd,  console = factory.start_application(host, port)
    beanstalkd.connect()
    console.main_loop()


if __name__ == "__main__":
    main(sys.argv[1:])
