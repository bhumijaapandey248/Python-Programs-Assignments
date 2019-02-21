#3. Read two input from STDIN (Standard Input) and print three lines where:
#a. The first line contains the sum of two numbers
#b. The second line contains the difference of two numbers (first - second)
#c. The third line contains the product of two number
#Input: 3 2
#Output: 5
#1
#6
#Note: The inputs must be taken as specified i.e. the first number and second number in input must be in a single line separated by a single space.

a,b=(input()).split(" ")
a=int(a)
b=int(b)
first=a+b
second=a-b
thrid=a*b
print(f"{first}\n{second}\n{thrid}")

