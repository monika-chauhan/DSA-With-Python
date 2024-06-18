def ToggleKthBit(N,K):
    mask = (1 << (K-1)) 
    return N ^ mask 

print(ToggleKthBit(5, 1))
print(ToggleKthBit(2, 3))
print(ToggleKthBit(75,4))
    