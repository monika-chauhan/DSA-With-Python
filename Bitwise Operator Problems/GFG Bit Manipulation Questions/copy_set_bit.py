'''Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.
Examples : 

Input  : x = 10, y = 13, l = 2, r = 3
Output : x = 14
Binary representation of 10 is 1010 and 
that of y is 1101. There is one set bit
in y at 3'rd position (in given range). 
After we copy this bit to x, x becomes 1110
which is binary representation of 14.

Input  : x = 8, y = 7, l = 1, r = 2
Output : x = 11'''

def copy_set_bit(x,y,l,r):
    if l < 1 or r > 32:
        return 0 
    
    for i in range(l,r+1):
        mask = 1 << (i-1)

        if y & mask != 0:
            x = x | mask 
    return x 

print(copy_set_bit(8,7,1,2))