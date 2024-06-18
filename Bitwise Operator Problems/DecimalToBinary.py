'''
n = 5 binary(n) = 101
i = 0 
bit = n & 1 => if right most bit 1 then bit = 1 else bit = 0 
Store ans = bit*pow(10,i) + ans 
then increment i += 1
then Right shift the n to get next right most bit  n = n >>
'''

def DecToBin(n):
    ans = 0 
    i = 0
    while n != 0:
        bit = n & 1
        ans += (bit * pow(10,i)) 
        n = n >> 1
        i += 1
    return ans 

print(DecToBin(10))