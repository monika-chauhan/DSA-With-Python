def SwapTwoNumber(a,b):
    print('previous a:',a, 'previous b:', b)
    a = a ^ b 
    b = a ^ b 
    a = a ^ b 
    return 'new a:',a, 'new b:',b 

print(SwapTwoNumber(2,3))