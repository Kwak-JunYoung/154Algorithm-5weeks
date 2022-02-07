a = [0] * 11

a[0] = 0
a[1] = 1
a[2] = 2
a[3] = 4

t = int(input())
for _ in range(t):
    n = int(input())
    if a[n] != 0:
        print(a[n])
        continue
    else:
        for i in range(4, n + 1):
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]
        print(a[n])