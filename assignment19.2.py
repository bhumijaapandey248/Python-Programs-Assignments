##2. Write a program using function sumOfDigits( n ) which returns the sum of digits of n.
##Input Format: The first line of input contains T, number of testcases. The only line of each test case contains the value of n.
##Output Format: For each test case in a new line, print the sum of digits of n.
##Input Example:
##3
##123
##2
##12
##Output:
##6
##2
##3

def sumOfDigits(n):
    sum=0
    for i in n:
        i=int(i)
        sum=sum+i
    print(sum)

t=int(input())
while(t>0):
    n=input()
    sumOfDigits(n)
    t=t-1
