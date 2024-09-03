'''Given an integer n, calculate the square of a number without using *, / and pow(). 

Examples : 

Input: n = 5
Output: 25

Input: 7
Output: 49

Input: n = 12
Output: 144
'''

def square(num):
    if num < 0:
        num = -num
    
    power, res = 0, 0 
    temp = num
    while temp != 0:
        if temp & 1:
            res += num << power 
        power += 1

        temp = temp >> 1
    return res 

print(square(12))
print(square(-12))