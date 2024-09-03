''' 1
    2 2
    3 3 3
    4 4 4 4 
    5 5 5 5 5 
'''

N = int(input("Enter the Number"))
for R in range(1,N+1):
    print(str(R)*R,end = '')
    print()


# Second approach 
N = int(input("Enter the Number"))
for R in range(1,N+1):
    for C in range(R):
        print(R, end = '')
    print()
