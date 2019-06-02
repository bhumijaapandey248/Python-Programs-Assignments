#https://practice.geeksforgeeks.org/problems/remove-duplicates/0


##str = input()
##count = {}
##for i in str:
##    count[i] = str.count(i)
##s = count.keys()
##s = list(s)
##for ele in s:
##    print(ele, end="")

def remove_duplicates(str):
    count = {}
    for i in str:
        count[i] = str.count(i)
    s = count.keys()
    s = list(s)
    for ele in s:
        print(ele, end="")

t = int(input())
while(t>0):
    str = input()
    remove_duplicates(str)
    print()
    t = t - 1
