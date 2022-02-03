from sys import stdin

N = int(stdin.readline().rstrip())

for _ in range(N):
    A, B = map(int, stdin.readline().split())
    print(A+B)