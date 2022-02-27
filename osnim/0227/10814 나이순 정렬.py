from sys import stdin

n = int(stdin.readline())

a = []

count = 1

for i in range(n):
    data = stdin.readline().split()

    a.append((int(data[0]), data[1], count))

    count += 1

a = sorted(a, key = lambda x : (x[0], x[2]))

for i in range(n):
    print(a[i][0], a[i][1])