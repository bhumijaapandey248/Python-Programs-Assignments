##3. Write a program for Binary Search using function that takes three parameters as s (size of array), arr (sorted array), n (number to be searched) and returns the index of the element (n).
##Input Example: -
##3
##5 1
##5 4 3 2 1
##5 1
##1 2 3 4 5
##8 12
##7 8 9 10 11 12 13 14
##
##Output Example: -
##Value not found !!
##0
##5

# Valid for increasing order array
def BinarySearch(size,a,x):

    start=0
    end=size-1
    mid=0
    while(start<=end):
       mid=(start+end)//2
       if(a[mid]==x):
           return (mid)
           break
       elif(x<a[mid]):
           end=mid-1
       elif(x>a[mid]):
           start=mid+1
    if(start>end):
        print("Value not found !!")


t=int(input())#test case
while(t>0):
    n=input().split()
    size=int(n[0])
    x=int(n[1])#Searched element
    str=input()
    lst=str.split()
    a=list(map(int,lst))
    index=BinarySearch(size,a,x)
    print(index)
    t=t-1
    



