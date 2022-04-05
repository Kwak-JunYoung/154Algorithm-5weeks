import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    for j in range(M):
        sys.stdout.write(str(i+j)+ " ")
    sys.stdout.write("\n")

print()