##2.Write a program using function that takes two numbers as input and returns the GCD.
##Input Example: -
##2
##5 10
##14 8
##Output Example: -
##5
##2

def GCD(num1,num2):
    while(num2!=0):
        r=num1%num2
        num1=num2
        num2=r
    return num1
t=int(input())
while(t>0):
    n=input().split()
    n1=int(n[0])
    n2=int(n[1])
##    print("n1",n1,"n2",n2)
    print(GCD(n1,n2))
    t=t-1


##def GCD(num1,num2):
##    while(num2!=0):
##        r=num1%num2
##        num1=num2
##        num2=r
##    return num1
##n1=int(input())
##n2=int(input())
##print(GCD(n1,n2))



