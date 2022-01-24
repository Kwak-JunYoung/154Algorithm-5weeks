n, k = list(map(int, input().split()))
l = [i for i in range(1, n+1)]
ind = 0
ans = []
while len(l):
    ind += (k-1)
    ind %= len(l)
    ans.append(str(l[ind]))
    l.remove(l[ind])

print("<", end ="")
print(", ".join(ans), end="")
print(">", end="")