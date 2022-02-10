n = int(input())

ar = []

for _ in range(n):
    ar.append(int(input()))

ar.sort()

for i in range(n):
    print(ar[i])


