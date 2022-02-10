from itertools import combinations
n, s = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    adv = (list(combinations(l, i)))
    for a in adv:
        if sum(a) == s:
            ans += 1

print(ans)