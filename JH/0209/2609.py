import sys

x, y = map(int, sys.stdin.readline().split())

def gcd(x,y):
    if y==0:
        return x
    else: 
        return gcd(y, x%y)

def lcm(x,y):
    g = gcd(x,y)
    return int(g * (x//g) * (y//g))

print(gcd(x,y))
print(lcm(x,y))

####내장 함수 (RuntimeError)
import math
x, y = map(int, input().split())

print(math.gcd(x,y))
print(math.lcm(x,y))