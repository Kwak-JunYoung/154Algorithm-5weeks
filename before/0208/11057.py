n = int(input())

a = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    a[0][i] = 1

for i in range(1, n + 1):
    for j in range(10):
        a[i][j] = sum(a[i - 1][j:])

print(a[n][0] % 10007)