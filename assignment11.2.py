#2. Write a program in python that takes two integers x, y and swap them without using third variable.

x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
x=x+y
y=x-y
x=x-y
print(f"value of x :{x}")
print(f"value of y :{y}")
