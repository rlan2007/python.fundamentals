#! /usr/bin/python3

import sys
import re

pattern = r"\b(\w)(\w)(\w*)\b"
repl = r"\2\1\3"

# Считываем все строки по одной из стандартного потока ввода
for line in sys.stdin:
    line = line.rstrip()
    # process line
    line = re.sub(pattern, repl, line)  
    print(line)
