'''Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

Example 1:

Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following M packets :{3, 4, 9, 7, 9}.
'''
'''Approach:
Sort the array = [1,3,4,7,9,9,12,56]
i=0   j=M-1   arr[i]  arr[j]        diff = min(diff,arr[j]-arr[i])
0      4        1       9               min('inf',(9-1)) = 8
1      5        3       9               min(8,(9-3)) = 6
2      6        4       12              min(6,(12-4)) = 6
3      7        7       56              min(6,(56-7)) = 6 

output = 6 
'''

def findMinDiff(A,N,M):
    A.sort()
    diff = float('inf')
    i = 0 
    j = M - 1
    while i < N and j < N:
        diff = min(diff,(A[j]-A[i]))
        i += 1
        j += 1
    return diff 

A = [1,3,4,7,9,9,12,56]
N = len(A)
M = 5
print(findMinDiff(A,N,M))