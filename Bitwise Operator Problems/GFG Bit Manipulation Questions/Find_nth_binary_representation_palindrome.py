'''Find the nth number whose binary representation is a palindrome. Do not consider the leading zeros, while considering the binary representation. Consider the 1st number whose binary representation is a palindrome as 1, instead of 0 

Examples: 

Input : 1
Output : 1
1st Number whose binary representation 
is palindrome is 1 (1)

Input : 9
Output : 27
9th Number whose binary representation
is palindrome is 27 (11011)
'''

# Find Kth set bit 
def iskthSetBit(N, k):
    return 1 if N & (1 << (k-1)) else 0 

# find leftmost set bit 
def LeftMostSetBit(N):
    count = 0 
    while N:
        count += 1
        N = N >> 1
    return count 

# check The number if its plaindrome

def isBinPalindrome(N):
    l = LeftMostSetBit(N)
    r = 1 
    while l > r:
        if iskthSetBit(N,l) != iskthSetBit(N,r):
            return 0 
        l -= 1
        r += 1
    return 1 

def nthPalindrome(N):
    pal_count = 0 
    for i in range(1, 2**31-1):
        if isBinPalindrome(i):
            pal_count += 1

        if pal_count == N:
            break 
    return i 

print(nthPalindrome(9))