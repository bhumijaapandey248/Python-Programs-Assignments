##3. Write a program using function swapElement( n, arr, k ) which swaps the kth element from the beginning with the kth element from the end and returns the array.
##Input Format: The first line of input contains an integer T denoting the number of testcases. Each testcase contains 2 lines of input; The first line of input contains N, k separated by a single space where N is the size of the array and k is the number for replacement. The second line contains N integers (elements of the array) separated with spaces.
##Output Format: For each test case, print the modified array.
##Input Example:
##1
##8 3
##1 2 3 4 5 6 7 8
##Output:
##1 2 6 4 5 3 7 8


def swapElement( n, arr, k ):
    temp=arr[k-1]
    arr[k-1]=arr[n-k]
    arr[n-k]=temp
    return arr
    
t=int(input("t"))    
while(t>0): 
    n1=input().split()
    n=int(n1[0])
    k=int(n1[1])
    str=input("ar")
    lst=str.split()
    arr=list(map(int,lst))
    index= swapElement(n, arr, k)
    print(index)
    t=t-1
