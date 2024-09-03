'''
    1 2 3 4 5  5 4 3 2 1
    1 2 3 4 * *  4 3 2 1
    1 2 3 * * * *  3 2 1
    1 2 * * * * * *  2 1
    1 * * * * * * * *  1
'''

N = int(input("Enter the Number"))
for R in range(N+1):
    start = 1 
    while start<=N-R:
        print(start,end=' ')
        start += 1
 

    star = R 
    if star == N:
        break 
    if star == 0:
        print(' ',end = ' ')
    else:
        print(2*R*' *'+' ',end = ' ')
    
    end = N-R 
    while end>=1:
        print(end,end=' ')
        end -= 1
    print() 


