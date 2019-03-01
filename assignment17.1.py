##1. Write a program that accepts a sentence and calculate the number of letters and digits.
##Example Input:
##Hello world! 123
##Output:
##LETTERS 10
##DIGITS 3


str=input()
letter=0
digit=0
for i in str:
    
    if i.isalpha():
        letter=letter+1
        
    elif i.isdigit():
        digit=digit+1
        
    else:
        pass
    
print(letter)
print(digit)
