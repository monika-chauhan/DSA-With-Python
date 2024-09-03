'''' A  = 10 , B = 20 
A = 1010 and B = 10100
0 1 0 1 0
1 0 1 0 0
----------
c,c,c,c
C = c+c+c+c = 4 ans  
''' 

def countFlipedBit(A,B):
    count = 0
    while A != 0 or B != 0:
        Abit = A & 1 
        Bbit = B & 1 
        if Abit != Bbit:
            count += 1
        A = A >> 1
        B = B >> 1
    return count 

print(countFlipedBit(10,20))
print(countFlipedBit(10,5))
print(countFlipedBit(2,6))