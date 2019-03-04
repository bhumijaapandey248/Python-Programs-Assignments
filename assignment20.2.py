##2. Write a program using function equalIndex( n, arr ) and return the value whose value is equal to that of its index value (starting with 1).
##Input Format: The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, size of array. The second line of each test case contains array elements.
##Output Format: Print the element whose value is equal to index value. Print "Not Found" when index value does not match with value.
##Example Input:
##2
##5
##15 2 45 12 7
##1
##1
##Output:
##2
##1
##Explanation:
##In the 1st testcase, 15 is at index 1, 2 is at index 2 and so on. So, we printed 2 because index
##matches with the number.

def equalIndex( n, arr ):
    
    for pos,element in enumerate(arr):
        if(pos+1==element):
            print(f"{element}")
        
t=int(input())
while(t>0):
    n=int(input())
    str=input()
    lst=str.split()
    arr=list(map(int,lst))
    equalIndex( n, arr )
    

##print(arr)


        
