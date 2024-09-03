def MinimumXorPairValue(arr):
    arr.sort()
    xor = 0 
    min_xor = float('inf')
    for i in range(len(arr)-1):
        xor = arr[i] ^ arr[i+1]
        min_xor = min(min_xor,xor)
    return min_xor

print(MinimumXorPairValue([9,5,3]))