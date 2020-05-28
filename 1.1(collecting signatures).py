n=int(input())
pot=[]
for i in range(n):
    a,b=map(int,input().split())
    pot.append((a,b))
pot.sort()
p=pot[0][0]
q=pot[0][1]
points=[]
for i,j in pot:
    if i<=q:
        p=i
        if j<q:
            q=j
    else:
        points.append(p)
        p=i
        q=j
points.append(p)
print(len(points))
print(*points)
