N = int(input())

for i in range(N, 0, -1):
    for _ in range(N-i):
        print(" ", end="")
    print("*" * (2 * i - 1))

for t in range(2, N+1):
    for _ in range(N-t):
        print(" ", end="")
    print("*" * (2 * t - 1))