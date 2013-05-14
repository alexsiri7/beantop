
import telnetlib

from beanstalkd import Beanstalkd
from beanstalkdstats import BeanstalkdStats
from console import Console


class Factory:
    @staticmethod
    def createTelnetConnection():
        return telnetlib.Telnet()
    @staticmethod
    def startApplication():
        t = Factory.createTelnetConnection()
        b = Beanstalkd(t)
        stats = BeanstalkdStats(b)
        console = Console()       
        return b, stats, console
