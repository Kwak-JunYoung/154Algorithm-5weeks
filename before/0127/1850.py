import math
a, b = list(map(int, input().split()))
x = math.gcd(a, b)
print('1' * x)