'''
    A B C 
    B C D 
    C D E
'''

N = int(input("Enter the number"))
num = 63 
for R in range(1,N+1):
    for C in range(1,N+1):
        print(chr(num+R+C),end = ' ')
    print()
