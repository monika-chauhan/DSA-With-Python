'''
    1 2 3 4
      2 3 4 
        3 4
          4 
'''

N = int(input("Enter the number"))
count = 1 
for R in range(1,N+1):
    for C in range(R,N+1):
        if C == R:
            print(C *' ',end = '')
        print(C ,end = '' )
    
    print()


