def C(n,k):
    if k>n:
        return 0
    elif k==0:
        return 1
    else:
        return  C(n - 1, k) + C(n - 1, k - 1)
n,k = (int(i) for i in input().split())
print (C(n,k))