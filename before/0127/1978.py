n = int(input())
l = list(map(int, input().split()))

x = max(l)
num=set(range(2, x + 1))

for i in range(2, x + 1):
    if i in num:
        num-=set(range(2 * i, x + 1, i))

ans = 0

for ll in l:
    if ll in num:
        ans += 1

print(ans)