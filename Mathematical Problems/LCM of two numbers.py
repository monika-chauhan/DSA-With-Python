import math 

def LCM(a,b):
    gcd = math.gcd(a,b)
    lcm = int(gcd / a*b) 
    return lcm 
print(LCM(7,35))