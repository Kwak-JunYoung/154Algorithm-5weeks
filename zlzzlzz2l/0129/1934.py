from math import gcd

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))
