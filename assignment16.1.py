##1. Write a program that accepts a comma-separated sequence of words as input and print the words in a comma-separated sequence after sorting them alphabetically.
##Input :without,hello,bag,world
##Output :bag,hello,without,world

str=input()
res=str.split(",")
res.sort()
print(res)





