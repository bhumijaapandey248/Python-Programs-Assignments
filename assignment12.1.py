##l=[]
##n=int(input())
##for i in range(1,n+1):
##    a=int(input(""))
##    l.append(a)
##print(f"Input List : {l}")
##r=int(input(" Given Value :"))
##for i in l:
##    if i>r:
##        print("yes")
##        continue
##    else:
##        print("No")
##        continue
##l=input()
##l=l.split()

##Input :3 4 5 6 7
##2
##Yes
##Input :3 4 5 6 7
##5
##No

str=input("Input :")

n=int(input())

lst=str.split()

lst=list(map(int,lst))

flag=True

for i in lst:
    if(i<n):
        flag=False

if(flag==True):
    print("Yes")
else:
    print("No")

