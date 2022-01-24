n = int(input())
for i in reversed(range(0, n)):
    print(" " * i + "*" * (2 * (n-i-1) + 1))
