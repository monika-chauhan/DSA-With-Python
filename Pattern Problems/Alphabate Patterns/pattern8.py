'''
    D 
    C D
    B C D 
    A B C D
'''

N = int(input("Enter the number")) # 4 

num = 64 # 
for R in range(N):
    for C in range(R+1):
        print(chr(num+N-C),end = ' ')  
    print()