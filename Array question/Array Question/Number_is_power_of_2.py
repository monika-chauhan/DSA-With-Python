def isNumberPowerOfTwo(number):
    if number == 0:
        return False 
    if number & (number-1) == 0:
        return True 
    else:
        return False 

print(isNumberPowerOfTwo(15))

