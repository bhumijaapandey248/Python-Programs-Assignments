##2. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphabetically.
##Input :hello world and practice make perfect and hello world again
##Output :again and hello make perfect practice world

str=input()
res=str.split()
s=set(res)
l=list(s)
l.sort()
for i in l:
    print(i,end=" ")
