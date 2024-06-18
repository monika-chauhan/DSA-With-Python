'''n = 18 bin(n) = 10010 
Set bit from right => at index 2 
'''

def SetBitFromRight(n):
    count = 0 
    while n != 0:
        bit = n & 1 
        count += 1
        if bit == 1:
            return count 
        n = n >> 1
    return 0 

print(SetBitFromRight(18))
print(SetBitFromRight(0))

# Second approach using Log Function 

import math 
n = 18
print("Using Log base of 2 Index of set bit from right:",int(math.log(2,n&-n)+1))