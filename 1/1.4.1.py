#!/bin/pithon3

space = {}
child = {}
out = []

space['global']=[]

#################################################
def create(namespace, parent):
    if namespace not in space:
        child[namespace] = parent
        space[namespace] = []       
    
def add(namespace, var):#добавить в пространство
    if namespace in space:
        space[namespace].append(var)        

def get(namespace, var):#вернуть пространство
    if namespace in space:
        if var in space[namespace]:
            out.append(namespace)
        elif namespace == 'global':
            out.append('None') 
        else:
            for key, value in child.items():
                if key == namespace:
                   get (value, var)
                   break
    else:
        out.append('None') 

#################################################
n = int (input())
for i in range(0, n):
    comand,nam,v  = input().split(' ')

    if comand == 'create':
        create (nam, v)
    elif comand == 'add':
        add (nam, v)
    elif comand == 'get':
        get (nam, v)
#################################################
for i in out:
    print (i, end='\n' )
