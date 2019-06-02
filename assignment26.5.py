#https://practice.geeksforgeeks.org/problems/count-smaller-elements/0

##n = int(input())
##arr1 = list(map(int,input().split()))
##sum = arr1[0]
##for i in range(0,n-1):
##    if(arr1[i]!=arr1[i+1]):
##            sum = sum + arr1[i+1]
##print(sum)

def sum_of_distinct_elements(n, arr):
    sum = arr[0]
    for i in range(0,n-1):
        if(arr[i]!=arr[i+1]):
                sum = sum + arr[i+1]
    return(sum)

t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    index = sum_of_distinct_elements(n, arr)
    print(index)
    t = t-1
