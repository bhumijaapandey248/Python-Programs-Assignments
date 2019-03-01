##1. Write a program to print all prime numbers between 1 and n (entered by the user).
##5
##10
##2 3 5 7 
##
##20
##2 3 5 7 11 13 17 19 
##
##25
##2 3 5 7 11 13 17 19 23 
##
##45
##2 3 5 7 11 13 17 19 23 29 31 37 41 43 
##
##50
##2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

def prime_number(n):
    for no in range(1,n+1):
        temp=0
        for i in range(1,no+1):
            if(no%i==0):
                temp=temp+1
        if(temp==2):
                print(no,end=" ")    
    print("\n")   
    

t=int(input())
while(t>0):
    n=int(input())
    prime_number(n)
    t=t-1

##def PrimeNumber(n):
##    for no in range(1,n+1):
##        temp=0
##        for i in range(1,no+1):
##            if(no%i==0):
##                temp=temp+1
##        if(temp==2):
##            print(no)
##        
##n=int(input())
##PrimeNumber(n)

##def PrimeNumber(n):
##    t=int(input("test case"))
##    while(t>0):
##        temp=0
##        for i in range(1,n+1):
##            if(n%i==0):
##                temp=temp+1
##        if(temp==2):
##            print("It is prime number !!")
##        else:
##            print("It is not prime number !!")
##        t=t-1
##        
##n=int(input())
##PrimeNumber(n)




##t=int(input(""))
##while(t>0):
##    n=int(input(""))
##       
##    for no in range(1,n+1):
##        temp=0
##        for i in range(1,no+1):
##            if(no%i==0):
##                temp=temp+1
##        if(temp==2):
##            print(no,end=" ")
##            
##    print("\n")   
##    t=t-1    
##    












