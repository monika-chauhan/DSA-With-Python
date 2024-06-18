'''
n = 101 as per normal math we have to multiply by pow of (2,i)
another way , We are providing the value as decimal it self So need to get the decimal as 101 -> 5 as answer
step1: ans = 0 , i = 0 
Step2: while n != 0:
Step3: digit = 101 % 10  # storing the remainder
Step4: ans = ans + pow(2,i)
step5 : n = n//10 
Step6: i += 1
step7: return ans 
 '''

def BinToDec(n):
    ans = 0 
    i = 0 
    while n != 0:
        dig = n % 10 # 1
    
        if dig == 1:
            ans += pow(2,i)
       
        n = n // 10 
        i += 1
    return ans

print(BinToDec(101))