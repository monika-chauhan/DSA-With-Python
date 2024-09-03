'''
    A 
    B C
    D E F 
    G H I J 
'''

N = int(input("Enter the Number"))
num = 65
for R in range(1,N+1):
    for C in range(R):
        print(chr(num),end = ' ')
        num += 1

    print()
