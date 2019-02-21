##3.Write a separate function that takes a number n and returns a dictionary that contains (i, i*i) where 1<= i <= n and prints the dictionary in the main function.
##Input Format: The only line of input takes a number n from user
##Output Format: The output prints the dictionary on the STDOUT.
##Example Input:
##8
##Output:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def keysquare(n):
        d={}
        for i in range(1,n+1):
            d[i]=i**2
        return d
num=int(input())
print(keysquare(num))
