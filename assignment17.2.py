##2. Write a function which will display all such numbers between 1000 and 3000 (both included) such that each digit of a number is an even. Call this function in the main function. The numbers obtained should be printed in a comma-separated sequence on a single line.

def even_num(n):
    flag=1
    temp=n
    while(n!=0):
        r=n%10
        if(r%2!=0):
            flag=0
            break
        n=n//10
    if(flag==1):
        print(temp,end=",")
for i in range(2000,3000):
    n=int(i)
    even_num(n)


##n=int(input())
##flag=1
##while(n!=0):
##    r=n%10
##    if(r%2!=0):
##        flag=0
##        break
##    n=n//10
##if(flag==1):
##    print("True")
##else:
##    print("False")



##def even_num(a)
##        l=[]
##        for i in range(2000,3000):
##            n=int(i)
##            flag=1
##            while(n!=0):
##                r=n%10
##                if(r%2!=0):
##                    
##                    flag=0
##                    break
##                n=n//10
##            if(flag==1):
##                print(n,end=",")
##
##even_num(n)
            


