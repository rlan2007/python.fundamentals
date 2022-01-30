#!/bin/python3
child = {}
exeptionList = []
out = []



#################################################
def javlaetsa(exepionList, potomok,child):
    for predok in exeptionList:
        if get (predok, potomok, child):
	        return True	
    return False
         
def get(predok, potomok,child):#вернуть пространство
    if predok == potomok:
        return True
    elif potomok in child:
        if predok in child[potomok]:                       
            return  True
        else:
            for value in child[potomok]:
                if  get(predok,value, child):
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
    potomok = input()	
    if javlaetsa(exeptionList,potomok,child):
        out.append(potomok)    	
    exeptionList.append(potomok)
	
    
#################################################
for i in out:
    print (i, end='\n' )
	
	
	
	
	
	
	












	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
