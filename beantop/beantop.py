from . import factory 
import sys

def main():
    arguments = factory.create_arguments_parser()
    host, port = arguments.process(sys.argv[1:])
    beanstalkd,  console = factory.start_application(host, port)
    beanstalkd.connect()
    console.main_loop()
