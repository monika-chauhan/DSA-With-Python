'''Given a non-negative number n and two values l and r. The problem is to count the number of set bits in the range l to r in the binary representation of n, i.e, to count set bits from the rightmost lth bit to the rightmost rth bit. 
Constraint: 1 <= l <= r <= number of bits in the binary representation of n.
Examples: 
 

Input : n = 42, l = 2, r = 5
Output : 2
(42)10 = (101010)2
There are '2' set bits in the range 2 to 5.

Input : n = 79, l = 1, r = 4
Output : 4
'''

'''We create the mask as => ((1>>r)-1) ^ (1>>(l-1)-1)
After this did And Operator-> num = N & mask and count the set bit in This num '''

def CountSetBitInRange(N, l, r):
    # Create a Number That is having r bits those are set bit in range of L to R in mask 
    mask = ((1 << r) - 1) ^ (1 << (l-1)-1)
    num = N & mask
    
    count = 0 
    while num != 0:
        bit = num & 1 
        if bit == 1:
            count += 1
        num = num >> 1
    return count 
print(CountSetBitInRange(42,2,5))
print(CountSetBitInRange(10,2,3))
