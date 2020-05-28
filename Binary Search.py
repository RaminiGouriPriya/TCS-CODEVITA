def binarysearch(arr,m,r,x):
    if r>=m:
        mid=m+(r-m)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,m,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1
arr=list(map(int,input().split(" ")))
x=list(map(int,input().split(" ")))
for i in x[1:]:
    print(binarysearch(arr[1:],0,len(arr)-2,i),end=" ")
    
