N = int(input())

for i in range(1, N + 1):
    for _ in range(N-i, 0, -1):
        print(" ", end="")
    print("*" * (2 * i - 1))