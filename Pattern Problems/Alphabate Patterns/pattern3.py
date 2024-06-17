'''
    A B C 
    D E F 
    G H I
'''

N = int(input("Enter the number"))
num = 65
for R in range(1,N+1):
    for C in range(1,N+1):
        print(chr(num),end = ' ')
        num += 1
    print()