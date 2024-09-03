'''Given an integer N, find its factorial. return a list of integers denoting the digits that make up the factorial of N.

Example 1:

Input: N = 5
Output: [1,2,0]
Explanation : 5! = 1*2*3*4*5 = 120
'''

def factorial(N):
    if N == 1:
        return 1 
    return N*factorial(N-1)

print(factorial(5))