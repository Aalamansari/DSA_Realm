def gcd(a,b):
    if a<0:
        a = a * -1
    if b<0:
        b = b * -1
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48,18))