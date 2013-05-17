
import telnetlib

import sys, getopt

import os, time, sys, termios, fcntl

from beanstalkd import Beanstalkd
from beanstalkdstats import BeanstalkdStats
from console import Console
from sysio import SysIO
from arguments import Arguments


class Factory:
    @staticmethod
    def createArgumentsParser():
        return Arguments(sys, getopt)
    @staticmethod
    def startApplication(host, port):
        t = telnetlib.Telnet()
        b = Beanstalkd(t, host, port)
        stats = BeanstalkdStats(b)
        console = Console(SysIO(os, time, sys, termios, fcntl), stats)       
        return b, console
