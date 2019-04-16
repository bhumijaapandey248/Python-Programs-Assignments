#https://practice.geeksforgeeks.org/problems/numbers-containing-1-2-and-3/0

def number_containing(n, a):
    for i in range(0,n+1):
        if(a[i]%10==1 or a[i]%10==2 or a[i]%10==3):
            print(a[i],end=" ")
    return(-1)

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    a = list(map(int,lst))
    index = number_containing(n, a)
    print(index)
    t = t-1
    
