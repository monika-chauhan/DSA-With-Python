# n = 11(decimal number)
# output = 3  (count the number of 1 bit in binary of n)

def NumberOfSetBits(n):
    count = 0 
    while n != 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count

n = 11 
print(NumberOfSetBits(n))
