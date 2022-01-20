objects = [5, 2, 1, 1, 1, 2, 3,[1,2,3],[1,2,3]]
ans = 0
for obj in range(len(objects)):
    raven = False
    for lev in range(obj):
        print (objects[lev],objects[obj],objects[lev] == objects[obj],'\n')
        if objects[lev] == objects[obj]: #if objects[lev] is objects[obj]:
            raven = True
            break
    if not raven:
        ans +=1    
print(ans)

