##2. You are given the year, and you have to write a function that takes a year as parameter and returns True or False (Boolean value) depending on whether the year is leap year or not. Print the returned value in the main function on the STDOUT.
##Input: 1990
##Output: False

def year(n):
    if (n%400==0) or (n%4==0) and (n%100!=0):
        print("True")
    else:
        print("False")
num=int(input())
year(num)
