import math

#02
def hypot(s1,s2):
    return math.sqrt(s1**2+s2**2)

print(hypot(3,4))

#03
def is_between(x,y,z):
    return ((x<y<z) or (z<y<x))

print(is_between(1,2,3))
print(is_between(3,2,1))
print(is_between(3,3,3))

#04
def ackermann(m,n):
    if m==0:
        return n+1
    elif (m>0) and (n==0):
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))

#print(ackermann(5,5))
print(ackermann(1,0))
print(ackermann(1,1))


print()
print()

#05
def gcd(a,b):
    if a % b == 0: return b
    return gcd(b,(a % b))

print(gcd(40,32))
print(gcd(32,40))
print(gcd(625,25))
print(gcd(25,625))
print(gcd(99,98))
print(gcd(98,100))