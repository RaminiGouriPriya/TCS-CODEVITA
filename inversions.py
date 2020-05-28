# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <=1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    a1=a[left:ave]
    b1=a[ave:right]
    i=0
    j=0
    l=left
    c=number_of_inversions
    print(a[left:ave],a[ave:right],number_of_inversions-c)
    while(i<len(a1) and j<len(b1)):
        if(a1[i]>b1[j]):
            a[l]=b1[j]
            l=l+1
            j=j+1
            number_of_inversions+=len(a1[i:])
        else:
            a[l]=a1[i]
            l=l+1
            i=i+1
           
    while(i<len(a1)):
        a[l]=a1[i]
        l=l+1
        i=i+1
        
    while(j<len(b1)):
        a[l]=b1[j]
        l=l+1
        j=j+1
        
    print(a,number_of_inversions-c)
    return number_of_inversions


b=int(input())
a = list(map(int, input().split(" ")))
    
print(get_number_of_inversions(a, b, 0, len(a)))
