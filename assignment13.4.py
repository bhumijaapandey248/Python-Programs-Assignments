#4. Read two integers and print two lines. The first line should contain integer division a//b. The second line should contain the float division a/b.
#You don’t need to perform any rounding off or formatting operation.
#Input: 4 3
#Output: 1
#1.33333333333

a,b=(input()).split()
a=int(a)
b=int(b)
second=a/b
first=a//b
print(f"{first}\n{second}")
