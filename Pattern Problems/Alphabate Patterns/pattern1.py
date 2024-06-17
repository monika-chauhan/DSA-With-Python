''' A A A
    B B B
    C C C 
''' 

# Capital Letter start from 65 
# Small Letter Start from 96 
N = int(input("Enter the number"))
for R in range(1,N+1):
    num = 64 
    for C in range(1,N+1):
        print(chr(num+R),end = ' ')
    print()