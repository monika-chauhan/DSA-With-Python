'''
    1 
    2 1
    3 2 1
    4 3 2 1
'''
N = int(input("enter the number"))
for R in range(1,N+1):
    value = R 
    for C in range(R):
        print(value,end = ' ')
        value -= 1 
    print()

# Second Approach 

N = int(input("Enter the Number"))
for R in range(1,N+1):
    for C in range(R):
        print(R-C,end = ' ')
    print()
