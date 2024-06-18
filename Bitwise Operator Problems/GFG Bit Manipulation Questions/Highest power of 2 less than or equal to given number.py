'''Given a number n, find the highest power of 2 that is smaller than or equal to n.

Examples : 

Input : n = 10
Output : 8

Input : n = 19
Output : 16

Input : n = 32
Output : 32
'''

def HighestPowerOfTwoLessThanN(n):
    ans = 1
    max_ans = 1  
    for i in range(31):
        ans = ans * 2 
        if ans <= n:
            max_ans = max(max_ans,ans)
    return max_ans

print(HighestPowerOfTwoLessThanN(10))
print(HighestPowerOfTwoLessThanN(32))