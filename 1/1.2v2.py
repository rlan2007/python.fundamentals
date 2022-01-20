objects = [1, 2, 1, 2, 3]

ans = 0
list = []
for obj in objects:
    if not obj in list:
        ans +=1
        list.append(obj)
    

print(ans)
