##3. Write a program that takes 2 numbers (R, C) as rows and columns separated by comma and generates a 2D-array. The element value of the ith row and jth column of the array should be i*j.
##Input: 3,5
##Output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

##from array import *
r=int(input())
c=int(input())
l1=[]
l2=[]
for i in range(0,r):
    for j in range(0,c):
        l1.append(i*j)
    l2.append(l1)
    l1=[]
print(l2)
