N = int(input())

for i in range(N, 0, -1):
    for _ in range(N - i, 0, -1):
        print(" ", end="")
    print("*" * i)