#https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0


##n = int(input())
##arr = list(map(int,input().split()))
##n1 = n//2
##sum1 = 0
##sum2 = 0
##for i in range(0,n1):
##    sum1 = sum1 + arr[i]
###print(sum1)
##
##for j in range(n1,n):
##    sum2 = sum2 + arr[j]
###print(sum2)
##
##mul = sum1 * sum2
##print(mul)

def multiply_left_right(n, arr):
    n1 = n//2
    sum1 = 0
    sum2 = 0
    for i in range(0,n1):
        sum1 = sum1 + arr[i]
    #print(sum1)

    for j in range(n1,n):
        sum2 = sum2 + arr[j]
    #print(sum2)

    mul = sum1 * sum2
    print(mul)

t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    multiply_left_right(n, arr)
    t= t - 1


    
