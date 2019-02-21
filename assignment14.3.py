##3. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
##Input Format:
##The first line contains n. The second line contains an array A[] of n integers separated by a space.
##Output:
##Print the runner-up score.
##Input: 5
##2 3 6 6 5
##Output: 5

str=input()
lst=str.split()
lst=list(map(int,lst))
s=set(lst)
lst2=list(map(int,s))
lst2.sort()
print(lst2[-2])

