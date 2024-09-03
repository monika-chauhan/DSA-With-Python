'''The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

  
n = 5 
mask = 0 
temp = n
while n != 0:
    right shift => n = n >> 1 # so that we count the number of 1's in number binary
    mask = (mask << 1 )| 1
return ~temp & mask '''

def Complement(n):
    temp = n 
    mask = 0 
    while n != 0:
        n = n >> 1
        mask = (mask << 1) | 1
    return ~temp & mask 
print(Complement(5))
print(Complement(7))
print(Complement(10))