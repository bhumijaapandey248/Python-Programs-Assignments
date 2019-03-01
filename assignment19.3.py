##3. Write a program using function getLCM( a, b) which returns the LCM of a,b.
##Input Format: The first line of input contains T, number of testcases. The only line of each test case contains two numbers a,b separated by a single space.
##Output Format: For each test case in a new line, print the LCM of a,b.
##Input Example:
##5
##1 5
##12 6
##8 20
##21 35
##5 1
##Output:
##5
##12
##40
##105
##5


def getLCM(n1,n2):
    while(n2!=0):
        r=n1%n2
        n1=n2
        n2=r
    res=n1
    lcm=(x*y)//res
    print(lcm)
    
t=int(input())
while(t>0):
    n=input().split()
    num1=int(n[0])
    x=num1
    num2=int(n[1])
    y=num2
    getLCM(x,y)
    t=t-1

