#3. Write a program in python that takes two float values from user and print the area of rectangle type casted to int.
#type cast float into integer

l=float(input("Enter the length of rectangle :"))
w=float(input("Enter the width of rectangle :"))
area=l*w
print(f"Area of rectangle :{area}")
print(int(area))
