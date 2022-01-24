import math

a, b = list(map(int, input().split()))
print(math.gcd(a, b))
print(a * b // math.gcd(a, b))