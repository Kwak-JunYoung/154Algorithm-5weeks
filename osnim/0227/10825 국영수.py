from sys import stdin

n = int(stdin.readline())

a = []

for i in range(n):

    data = stdin.readline().split()

    a.append((data[0], int(data[1]), int(data[2]), int(data[3])))

a = sorted(a, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(a[i][0])