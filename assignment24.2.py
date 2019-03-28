#https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0



            
def pairs_sum(a, m, b, n, x):
    for i in range(0,a):
        for j in range(0,b):
            if(m[i]+n[j]==x):
                print(m[i],n[j],end=",")
                print()

t= int(input())
while(t>0):
    r = input().split()
    a = r[0]
    a = int(a)
    b = r[1]
    b = int(b)
    x = r[2]
    x = int(x)
    s1 = input()
    lst1 = s1.split()
    m = list(map(int,lst1))
    s2 = input()
    lst2 = s2.split()
    n = list(map(int,lst2))
    pairs_sum(a, m, b, n, x)
    t = t-1




