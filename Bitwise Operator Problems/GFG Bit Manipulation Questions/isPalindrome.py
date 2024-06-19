def binary(N):
    ans = ''
    while N > 0:
        ans = (str(N&1)) + ans
        N >>= 1; 
    return ans; 

def isPalindorme(N):
    binN = binary(N) 
    if binN == binN[::-1]:
        return True
    else:
        return False

print(isPalindorme(17))
print(isPalindorme(10))

