''' 1 2 3
    4 5 6 
    7 8 9
'''

N = int(input("Enter the Number"))
count = 1 
for R in range(N):
    for C in range(N):
        print(count, end = '')
        count += 1
    print()
    