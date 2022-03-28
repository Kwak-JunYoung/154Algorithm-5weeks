import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
SUM = 0
result = 0

for i in range(N):
   SUM = a[i] + SUM
   result += SUM

print(result)