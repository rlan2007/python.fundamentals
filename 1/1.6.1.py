#!/bin/python3

child = {}
out = []


#################################################
def javlaetsa(predok, potomok):
    if get(predok, potomok):
        out.append('Yes')
    else:
         out.append('No')
         
def get(predok, potomok):#вернуть пространство
    if predok == potomok:
        return True
    elif potomok in child:
        if predok in child[potomok]:                       
            return  True
        else:
            for value in child[potomok]:
                if  get(predok,value):
                    return True             
            return False
    else:         
        return False
#################################################
n = int (input())
for i in range(0, n):
    klass = input().split(' ')
    child[klass[0]] = klass[2:]
n = int (input())
for i in range(0, n):
    predok ,potomok  = input().split(' ')
    javlaetsa(predok,potomok)

   
      
#################################################
for i in out:
    print (i, end='\n' )


