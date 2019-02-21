#2. Write a program to check if the list is sorted or not. Print YES if the list is already sorted and NO if it is not sorted.

l=[]
flag=0
n=int(input("Size :"))
for i in range(1,n+1):
    a=int(input(""))
    l.append(a)
print(f"Input Values {l}")
if (l==sorted(l)):
    flag=1
if(flag):
    print("yes")
else:
    print("no")











