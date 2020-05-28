# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    
    return j

def partition3(a, l, r):
    x=a[l]
    j=l
    for i in range(l+1,r+1):
        if(a[i]<=x):
            j=j+1
            a[i],a[j]=a[j],a[i]
    a[l], a[j] = a[j], a[l]
    k=j
    while(k!=-1 and x==a[k]):
        k=k-1
    return [k,j+1]
def randomized_quick_sort(a, l, r):
    #print(l,r,a)
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    #print(m,n)
    randomized_quick_sort(a, l, m);
    randomized_quick_sort(a, n, r);



n=int(input())
a = list(map(int, input().split(" ")))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
