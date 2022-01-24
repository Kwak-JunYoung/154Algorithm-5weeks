n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.extend(b)
a.sort()
for aa in a:
    print(aa, end = ' ')