'''
       *
      **
     ***
    ****
'''

N = int(input("Enter the number"))

for R in range(1,N+1):
    print((N-R)* ' ' + R*'*',end = '')
    print()
