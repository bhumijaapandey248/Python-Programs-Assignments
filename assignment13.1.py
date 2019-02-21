#1. There are times when all the inputs are provided in a single line and are separated by spaces. In such cases, the input() function takes the whole line as input and treats the line as a single input. We can use input().split() functionality to split the string into multiple words.
#In this question, you will take input a single line string comprised of string, int, and float. You'll split the string and assign string to s, int to i, and float to f. Print a final string comprised of s and (i+f)
#Input: Ram 2 2.3445
#Output: Ram 4.3445

s,i,f=input().split()
i=int(i)
f=float(f)
re=i+f
re=float(re)
print(f"{s} {re}")
