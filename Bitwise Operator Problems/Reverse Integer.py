'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

def ReverseInteger(x):
    ans = 0 
    max_int = 2**31 - 1
    min_int = -2**31

    while x != 0:
        if x < 0:
            dig = x % -10
        else:
            dig = x % 10 
        
        if max_int < ans * 10 + dig or min_int > ans*10+dig:
            return 0 
        print(dig,ans)
        ans = ans * 10 + dig 
        x = int(x*1.0/10)
    return ans 

n = 123 
print(ReverseInteger(n))
m = -123
print(ReverseInteger(m))
x = 120
print(ReverseInteger(x))
