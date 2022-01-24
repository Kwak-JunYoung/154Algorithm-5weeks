n = int(input())
p = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans += sum(p[:i + 1])
print(ans)