'''Given a number N, the task is to clear the K-th bit of this number N. If K-th bit is 1, then clear it to 0 and if it is 0 then leave it unchanged.
Examples: 
 

Input: N = 5, K = 1
Output: 4
5 is represented as 101 in binary
and has its first bit 1, so clearing
it will result in 100 i.e. 4.

Input: N = 5, K = 2
Output: 5
5 is represented as 101 in binary
and has its second bit is already 0,
so clearing it will result in 101 i.e. 5.'''

def ClearKthBit(N, K):
    return N & ~(1 << (K-1))
   
print(ClearKthBit(5,1))
print(ClearKthBit(6,3))