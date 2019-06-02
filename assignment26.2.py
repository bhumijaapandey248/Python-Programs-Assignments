#https://practice.geeksforgeeks.org/problems/count-smaller-elements/0


n = int(input())
arr = list(map(int,input().split()))
e = []
flag=1
for i in range(0,n):
    for j in range(1,n):
        if (arr[i]>arr[j]):
            e.append(arr[j])

    r = len(e)
    print(r)
##    e = []
r=0
