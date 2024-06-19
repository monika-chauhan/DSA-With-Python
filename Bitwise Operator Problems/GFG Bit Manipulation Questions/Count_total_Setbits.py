'''You are given a number n. Find the total number of set bits in the numbers from 1 to n. 
Example 1:

Input: n = 3
Output: 4
Explaination: 
1 -> 01, 2 -> 10 and 3 -> 11. 
So total 4 setbits.'''


def getSetBitsFromOneToN(n):
    N = n 
    two = 2 
    ans = 0 
    while n != 0:
        ans  += int(N/two) * (two >> 1)
        
        if N & (two - 1) > (two >> 1) - 1:
            ans += N & (two - 1) - (two >> 1) + 1
        
        two <<= 1
        n >>= 1
    return ans 

print(getSetBitsFromOneToN(10))