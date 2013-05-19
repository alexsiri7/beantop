
import telnetlib

import sys, getopt

import os, time, termios, fcntl

from beanstalkdstats import BeanstalkdStats
from beanstalkd import Beanstalkd
from console import Console
from sysio import Time,  CharReader,  ScreenPrinter
from arguments import Arguments



def create_arguments_parser():
    return Arguments(sys, getopt)
    
def start_application(host, port):
    telnet = telnetlib.Telnet()
    beanstalkd = Beanstalkd(telnet, host, port)
    stats = BeanstalkdStats(beanstalkd)
    char_reader = CharReader(os, sys, termios, fcntl)
    screen_printer = ScreenPrinter(os, sys)
    console = Console(Time(time),  char_reader,  screen_printer, stats)       
    return beanstalkd, console
