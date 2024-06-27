def gcd(a,b):
    if a % b == 0:
        return b 
    return gcd(b,a%b)

print(gcd(1,18))
print(gcd(5,25))
print(gcd(6,3))