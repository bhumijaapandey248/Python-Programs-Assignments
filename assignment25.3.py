#https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array/0


def move_all_zero(n, a):
    b1 = []
   
    for i in range(0,n):
        if a[i]!=0:
            b1.append(a[i])
##    print(b1,end=" ")
    for i in range(0,n):
        if a[i]==0:
            b1.append(a[i])
    for i in b1:
        print(i,end=" ")
            

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    a = list(map(int,lst))
    move_all_zero(n, a)
    print()
##    print(index)
    t= t- 1



##        print(a[i],end=",")
##a1 = len(a[i])
##print(a1)
##    size = len(a)
##    print(size)



##for i in range(0,n):
##    if a[i]==0:
##        count= count+1
##c = count
##print(c)
##for i in range(0,n+1):
##    a.remove(0)
##    print(a)
