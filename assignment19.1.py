##1. Write a program using function reverse(n) which returns the reverse of n.
##Input Format: The first line of input contains T, number of testcases. The only line of each test case contains the value of n.
##Output Format: For each test case in a new line, print the reverse of n.
##Input Example:
##5
##123
##21
##11
##7
##121
##Output:
##321
##21
##11
##7
##121

def reverse_number(n):   
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev)

t=int(input())
while(t>0):
    n=int(input())
    reverse_number(n)
    t=t-1
