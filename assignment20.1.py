##1. Write a program using function fibonacci(n) which returns the sum of fibonacci series up to n.
##Input Format: The first line of input contains T, number of testcases. The only line of each testcase contains the value of n.
##Output Format: For each testcase in a new line, print the sum of fibonacci series upto n.
##Input Example:
##3
##5
##7
##10
##Output:
##7
##20
##88


def fibonacciSum(n):
    if(n==1):
        return 0
    elif(n==2):
        return (0+1)
    else:
        a=0
        b=1
        sum=1
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
            sum=sum+b
        return(sum)
t=int(input())
while(t>0):
    n=int(input())
    print(fibonacciSum(n))
    t=t-1










