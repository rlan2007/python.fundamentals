#! /usr/bin/python3
import itertools

#генератор простых чисел
def primes():
  n = 2
  yield n
  while(True):
    n += 1
    count = 0
    for d in range(2, n//2+1):
      if n % d == 0:
        count += 1
        break
    if count == 0:
      yield n


#Пример использования:  

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

