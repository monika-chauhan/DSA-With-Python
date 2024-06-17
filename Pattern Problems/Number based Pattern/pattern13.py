'''
          1 
        2 3
      4 5 6    
    7 8 9 10   
'''

N = int(input("Enter the Number"))
count = 1
for R in range(1,N+1):
    space = N - R 
    while space:
        print(' ',end = ' ')
        space -= 1
    i = 1
    while i <= R:
        print(count,end = ' ')
        count += 1
        i += 1
    
    print()
        

        
