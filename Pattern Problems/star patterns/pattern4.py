'''
    ****
     ***
      **
       *
'''

N = int(input("Enter the number"))
for R in range(N,0,-1):
    print((N-R)*' '+ R*'*' ,end = '')
    print()