def countSetBit(N):
    count = 0 
    while N != 0:
        bit = N & 1
        if bit == 1:
            count += 1
        N = N >> 1
    return count 

print(countSetBit(5))
print(countSetBit(15))