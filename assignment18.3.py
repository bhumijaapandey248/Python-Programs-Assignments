##3. Write a program for Binary Search using function that takes three parameters as s (size of array), arr (sorted array), n (number to be searched) and returns the index of the element (n).

def BinarySearch(n):

    a=[]
    for i in range(1,n+1):
        elements=int(input("array elements"))
        a.append(i)
    x=int(input("Search"))
    start=0
    end=n-1
    mid=0
    while(start<=end):
       mid=(start+end)//2
       if(a[mid]==x):
           print("value found at "+str(mid)+" place !!")
           break
       elif(x<a[mid]):
           end=mid-1
       elif(x>a[mid]):
           start=mid+1
    if(start>end):
        print("Value not found !!")

size=int(input("Size"))


BinarySearch(size)
