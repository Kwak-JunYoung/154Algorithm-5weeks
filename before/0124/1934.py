import math
t = int(input())
ans = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    ans.append(a * b // math.gcd(a, b))

for a in ans:
    print(a)