#! /usr/bin/python3

import os
import os.path

ans = []
#sample = "sample"
sample = "main"

for curent_dir, dirs, files in os.walk(sample):
  print(curent_dir,':')
  for d in dirs:
    print(d)
  for f in files:
    print(f)
    if f[-3:]==".py": 
      ans += [curent_dir]
      break

ans.sort()
res = "\n".join(ans)
f = open("result.txt", "w")
f.write(res)
f.close()

