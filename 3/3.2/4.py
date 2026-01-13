#! /usr/bin/python3

import sys
import re

pattern = r"\\"

#Считываем все строки по одной из стандартного потока ввода
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(pattern, line):  print(line,"+")
