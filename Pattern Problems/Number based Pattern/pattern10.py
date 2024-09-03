'''
          1 
        2 2
      3 3 3
    4 4 4 4
'''

N = int(input("Enter the Number"))
for R in range(1,N+1):
    print((N-R)*' '+str(R)*R,end = ' ')
    print()

