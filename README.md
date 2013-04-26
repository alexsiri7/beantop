beantop
=======

Top command for [beanstalkd][]

[beanstalkd]: http://kr.github.com/beanstalkd/

=======
Usage: ./beantop.py -h <host> -p <port>

Inspired in very useful command tools like htop and innotop, I decided a good top command for beanstalkd could be very useful. Right now, it only shows a subset of the information available at a specified interval.

To exit, press 'q'

Example output:

    Thu, 25 Apr 2013 09:44:29
    current-jobs-ready: 0
    current-waiting: 89
    current-workers: 120
    
    Tube                     my_tube
         current-jobs-delayed              0
           current-jobs-ready              0
        current-jobs-reserved             31
              current-waiting             69

