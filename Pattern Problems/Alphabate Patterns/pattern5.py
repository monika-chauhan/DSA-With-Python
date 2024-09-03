'''
    A 
    BB
    CCC
    DDDD
'''

N = int(input("enter the number"))
num = 64 
for R in range(1,N+1):
    for C in range(R):
        print(chr(num+R),end = ' ')
    print()