#4. Write a program in python to take a string str and number num from the user and print the same string multiple times(num) with a space between each string.
#Input: str: Ram
#Num: 5
#Output: Ram Ram Ram Ram Ram

s=(input("str :"))
n=int(input("n :"))
for i in range(1,n+1):
    print(s,end=" ")

