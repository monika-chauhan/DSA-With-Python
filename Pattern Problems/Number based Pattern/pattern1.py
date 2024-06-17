''' 1 2 3 4 
    1 2 3 4 
    1 2 3 4 
    1 2 3 4 
'''

N = int(input("Enter the Number"))
for R in range(N):
    for C in range(N):
        print(C+1, end = '')
    print() 
