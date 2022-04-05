import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
SUM = a[0]

for i in range(1, N):
    for j in range(i+1):
        SUM += a[j]

print(SUM)