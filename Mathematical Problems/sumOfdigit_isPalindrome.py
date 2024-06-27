def sumOfDigit(n):
    sum = 0 
    while n != 0:
        rem = n % 10 
        sum += rem 
        n = n // 10 
    return sum 

def isPalindrome(n):
    num = sumOfDigit(n)
    temp = num 
    rev = 0 
    while num != 0:
        rem = num % 10 
        rev = rev * 10 + rem 
        num = num // 10
    if rev == temp:
        return 1 
    else:
        return 0 
    
print(isPalindrome(56))
print(isPalindrome(98))