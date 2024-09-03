'''
          1
        1 2 1
      1 2 3 2 1
    1 2 3 4 3 2 1
'''

N = int(input("enter the number"))
for R in range(1,N+1):
  # Print Space 
  space = N - R 
  while space:
    print(' ',end = ' ')
    space -= 1

  # Print First Triangle 
  j = 1 
  while j <= R:
    print(j,end = ' ')
    j += 1


  # Print Last Triangle
  start = R - 1
  while start:
    print(start, end = ' ')
    start -= 1
  print() 
  