#https://practice.geeksforgeeks.org/problems/pairs-with-positive-negative-values/0

n = int(input())
s = input()
lst = s.split()
a = list(map(int,lst))
a1 = []
a2 = []
for i in a:
    if (i > 0):
        a1.append(i)
        a1.sort()

print(a1)
for j in a:
    if (j < 0):
        a2.append(j)
        a2.sort(reverse=True)
print(a2)

for i in range(0,n):
    for j in range(1,n):
        if(a1[i]==a2[j]):
            print(a1[i],a2[j])
        
##            print(a[i],a[j])
####            print(a[j])
##print(0)
