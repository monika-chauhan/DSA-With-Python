'''
    A 
    B C 
    C D E
    D E F G
'''

N = int(input("enter the Number"))
num = 64
for R in range(1,N+1):
    for C in range(R):
        print(chr(num+R+C),end = ' ')
    print()