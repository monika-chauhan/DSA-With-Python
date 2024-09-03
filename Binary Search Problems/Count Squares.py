'''Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. You are given a number N, you have to output the number of integers less than N in the sample space S.

 

Example 1:

Input :
N = 9
Output:
2
Explanation:
1 and 4 are the only Perfect Squares
less than 9. So, the Output is 2.
'''

def countSquare(n):
    if n == 1:
        return 0 
    left = 1
    right = n 
    ans = 0
    while left <= right:
        mid = (left+right)//2 
        if mid * mid == n:
            return mid - 1
        elif mid * mid < n:
            ans = mid 
            left = mid + 1
        else:
            right = mid - 1
    return ans 
n = 9 
print(countSquare(n))