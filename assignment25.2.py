#https://practice.geeksforgeeks.org/problems/pairs-with-positive-negative-values/0

def positive_negative(n, a):
    a1 = []
    a2 = []
    for ele in a:
        if (ele > 0):
            a1.append(ele)
            a1.sort()
    l1 = len(a1)
    for ele in a:
        if (ele < 0):
            a2.append(ele)
            a2.sort(reverse=True)
    l2 = len(a2)
    flag = 0 # answer not found
    for i in range(0,l1):
        for j in range(0,l2):
            if(a1[i]==(-1*a2[j])):
                print(a2[j],a1[i],end=" ")
                flag = 1 ##answer found
    if(flag==0):
        print(0)
    print()
t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    a = list(map(int,lst))
    positive_negative(n, a)
    t = t-1
