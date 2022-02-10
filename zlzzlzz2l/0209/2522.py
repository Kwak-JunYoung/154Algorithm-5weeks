N = int(input())

for i in range(1, N+1):
    for _ in range(N-i, 0, -1):
        print(" ", end="")
    print("*" * i)

for t in range(N-1, 0, -1):
    for _ in range(N-t):
        print(" ", end="")
    print("*" * t)