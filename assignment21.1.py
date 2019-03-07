##Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
##
##Input:
##The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.
##
##Output:
##Print the missing number in array.
##
##Constraints:
##1 ≤ T ≤ 200
##1 ≤ N ≤ 107
##1 ≤ C[i] ≤ 107
##Input:
##2
##5
##1 2 3 5
##10
##1 2 3 4 5 6 7 8 10
##
##Output:
##4
##9


def missingNumber(N , arr):
    sum1=0
    sum2=0
    n=int(N)-1
    for i in range(1,N+1):
        sum1=sum1+i

    for i in range(0,n):
        sum2=sum2+arr[i]

    ans=sum1-sum2
    return ans

t=int(input())
while(t>0):
    N=int(input())
    str=input()
    lst=str.split()
    arr= list(map(int,lst))
    index= missingNumber(N , arr)
    print(index)
    t=t-1
    
