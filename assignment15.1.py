##1. Read an integer N. Print the square of all numbers less than N.
##Input: 5
##Output:
##1
##4
##9
##16


def square(i):
    sq=i**2
    return sq


n=int(input())
for i in range(1,n):
    sq=square(i)
    print(sq)



