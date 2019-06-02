#https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1-elements-1/0


n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

for i in range(0,n+1):
    if(arr1[i]!=arr2[i+1]):
        return(arr1[i])
            

##dif = (set(arr1)-set(arr2))
##dif = list(dif)
##dif1 = str(dif)
##
##print(dif)
##for i in range(0,n):
####    print(arr1[i])
##    if(arr1[i]==dif):
##        print(arr1[i])
##
##for i in range(0,n):
##    if arr1[i]!=arr2[i]:
##        print(arr1[i])
