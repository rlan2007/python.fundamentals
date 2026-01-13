#! /usr/bin/python3

s, a, b = [input() for x in range(3)]
count = 0

while(a in s):
  s = s.replace(a,b)
  count+=1
  if count >1000: 
    count = "Impossible"
    break

print(count)

input()