from simplecrypt import *
with open("encrypted.bin", "rb") as inp, \
open("passwords.txt", "r") as pas:
  encrypted = inp.read()
  passwords = pas.read().split()
  text = ''
  for str in passwords:
    try:
      text = decrypt(str, encrypted)
    except :
      print ('(:()')
  
  print (text)
print('done') 
input()  
