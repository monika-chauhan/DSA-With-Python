'''
    A B C 
    A B C 
    A B C
'''

N = int(input("Enter the number"))
for R in range(1,N+1):
    num = 64
    for C in range(1,N+1):
        print(chr(num+C),end = ' ')
    print()