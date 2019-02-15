l=[]
flag=0
n=int(input("Enter the size of list elements :"))
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











