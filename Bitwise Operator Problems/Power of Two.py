def PowerOfTwo(n):
    ans = 1
    for i in range(0,31):
        if ans == n:
            return True 
        ans = ans * 2 

    return False 

print(PowerOfTwo(4))
print(PowerOfTwo(1))
print(PowerOfTwo(3))