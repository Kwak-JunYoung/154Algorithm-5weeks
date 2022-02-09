n = int(input())

for i in range(1, n + 1):
    if i == n or i == 1:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")