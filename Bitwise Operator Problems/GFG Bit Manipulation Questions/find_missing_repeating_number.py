def missing_repeating(arr,n):
    xor = 0 
    x,y = 0, 0 
    for i in range(n):
        xor ^= arr[i] 
    
    for i in range(1,n+1):
        xor = xor ^ i 
    
    set_bit = xor & ~(xor-1)

    for num in arr:
        if num & set_bit != 0:
            x = x ^ num
        else:
            y = y ^ num
    
    for i in range(1,n+1):
        if i & set_bit != 0:
            x ^= i 
        else:
            y ^= i 
    
    result = []
    for i in range(n):
        if arr[i] == x:
            result.append(x)
            result.append(y)
            break 
        elif arr[i] == y:
            result.append(y)
            result.append(x)
            break 
    return result

print(missing_repeating([2,2],2))
print(missing_repeating([3,1,3],3))