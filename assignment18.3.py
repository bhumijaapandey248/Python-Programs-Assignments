##3. Write a program for Binary Search using function that takes three parameters as s (size of array), arr (sorted array), n (number to be searched) and returns the index of the element (n).

def BinarySearch(n):

    start=0
    end=n-1
    mid=0
##    x=int(input("x "))#"Search"
    while(start<=end):
       mid=(start+end)//2
       if(a[mid]==x):
           print(mid+1)
           break
       elif(x<a[mid]):
           end=mid-1
       elif(x>a[mid]):
           start=mid+1
    if(start>end):
        print("Value not found !!")


t=int(input("testcase "))#"test"
while(t>0):
    n=input().split()
    size=int(n[0])
    x=int(n[1])
##    size=int(input("size "))#"Size"
    str=input("ar")
    lst=str.split()
    a=list(map(int,lst))
    BinarySearch(size)
    t=t-1
    






