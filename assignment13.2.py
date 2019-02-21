#2. Given an integer n, perform the following conditional actions:
#a. If n is odd, print Weird
#b. If n is even and in the inclusive range of 2 to 5, print Not Weird
#c. If n is even and in the inclusive range of 6 to 20, print Weird
#d. If n is even and greater than 20, print Not Weird
#Input: 3
#Output: Weird

n=int(input())
if(n%2!=0):
    print("Weird")
else:    
    if(n>=2 and n<=5):
        print("Not weird")
    elif(n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")
