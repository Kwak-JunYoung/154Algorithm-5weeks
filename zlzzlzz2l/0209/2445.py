N = int(input())

for i in range(1, N + 1):
    print("*" * i, end="")
    for _ in range(N - i, 0, -1):
        print(" ", end="")
    for _ in range(N - i, 0, -1):
        print(" ", end="")
    print("*" * i, end="")
    print("")

for t in range(N-1, 0, -1):
    print("*" * t, end="")
    for _ in range(N - t, 0, -1):
        print(" ", end="")
    for _ in range(N - t, 0, -1):
        print(" ", end="")
    print("*" * t, end="")
    print("")