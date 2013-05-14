
import telnetlib

from beanstalkd import Beanstalkd
from beanstalkdstats import BeanstalkdStats
from console import Console
from sysio import SysIO


class Factory:
    @staticmethod
    def createTelnetConnection():
        return telnetlib.Telnet()
    @staticmethod
    def startApplication():
        t = Factory.createTelnetConnection()
        b = Beanstalkd(t)
        stats = BeanstalkdStats(b)
        console = Console(SysIO())       
        return b, stats, console
