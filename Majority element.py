def ME(n,A):
    D={}
    for i in A:
        D[i]=D.get(i,0)+1
        if(D[i]>n/2):
            return 1
    return 0
n=int(input())
arr=list(map(int,input().split(" ")))
print(ME(n,arr))
