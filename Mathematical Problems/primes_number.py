import math 

def isPrime(n):
    flag = 0 
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            flag = 1
            break 
    
    if flag == 1:
        return False 
    else:
        return True 

print(isPrime(24))
print(isPrime(31))