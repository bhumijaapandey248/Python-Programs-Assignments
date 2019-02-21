##3. Write a program that takes a sequence of comma separated integers from console and generate a list and a tuple that contains every number.
##Input Format: The only line of input takes a sequence of comma separated integers.
##Output Format: The first line of output displays the list and second line of output displays the tuple.
##Example Input:
##34,67,55,33,12,98

str=input()
res=str.split(",")
## list return krta h
res=list(map(int,res))
print(res)
res=tuple(map(int,res))
print(res)
##res=set(map(int,res))
##print(res)

