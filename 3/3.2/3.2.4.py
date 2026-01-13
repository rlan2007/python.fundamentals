import re
import sys
pattern = r".{0,}\\.{0,}"
for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(pattern, line) is not None:
        print(line)
