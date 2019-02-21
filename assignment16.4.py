##4. Write a program that takes a line as input and converts all lower-case letters to upper case and all upper-case letters to lower-case and spaces to $.
##Input Example:
##My NaMe is KhaN.
##Output:
##mY$nAmE$ISkHAn.


res=input()
rstr=''

for i in res:
    if(i.isupper())==True:
        rstr=rstr+(i.lower())

    elif(i.islower())==True:
        rstr=rstr+(i.upper())

    elif(i.isspace())==True:
        rstr=rstr+'$'

print(rstr)


