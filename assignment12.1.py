#1. Write a program in python to check if all the values in the list are greater than the given value (user defined). Print YES if all the values are greater than the given value and NO if not.
#Input: List [10, 20, 30, 40, 50]
#Given value = 20
#Output: NO
#Input: List [10, 20, 30, 40, 50]
#Given value = 5
#Output: YES
    
    
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

