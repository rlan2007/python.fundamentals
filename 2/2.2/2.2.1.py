#!/bin/python3

import datetime



d1,d2,d3 =  (int (i) for i in  (input().split()))
d = datetime.date (d1,d2,d3)

dni = int (input())

d = d + datetime.timedelta(days=dni)

print (d.year, d.month, d.day)

