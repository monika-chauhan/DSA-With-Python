'''
    1
    2 3
    3 4 5
    4 5 6 7
'''

N = int(input("Enter the number"))
for R in range(1,N+1):
    for C in range(R):
        print(R+C,end = ' ')
    print()
 
