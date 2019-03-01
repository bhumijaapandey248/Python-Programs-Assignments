##4. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. The output will be comma-separated numbers.
##Example Input:
##1,2,3,4,5,6,7,8,9
##Output:
##1,9,25,49,81

##str=input()
##
##res=str.split(",")
####l=[]
####print(type(res))
##for i in int(res):
##    if (int(i)%2!=0):
##        print(i**2)
##  
##
####l=[i**2 for i in str if i%2!=0]
####print(l)



str=input()
res=str.split(",")
for i in res:
    s1=int(i)
    if s1%2!=0:
        print(s1**2,end=',')

    else:
        pass














