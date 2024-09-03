''' 11111
    22222
    33333
    44444
'''

N = int(input("Enter the Number"))
for R in range(N):
    for C in range(N):
        print(R+1, end = '')
    print()