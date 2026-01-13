#! /usr/bin/python3

s, t = [input() for x in range(2)]
count = 0

def kount(str,sub):
  if (len(str) == 0) or ( not(sub in str) ): return 0
  pos = str.find(sub) + 1
  return 1 + kount(str[pos:], sub) 

print( kount(s,t) )

input()