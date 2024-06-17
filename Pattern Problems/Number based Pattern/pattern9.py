'''
    1 1 1 1 
      2 2 2
        3 3 
          4
'''

N = int(input("Enter the Number"))
for R in range(1,N+1):
    print(R*' '+(N-R+1)*str(R),end = '')
    print()
