#!/bin/python3

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list,Loggable):
    def append(self,v):
        self.log(v)
        super(LoggableList, self).append(v)


a = LoggableList()
a.append('msg 1')

a.append('msg 2')

