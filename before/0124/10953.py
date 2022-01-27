t = int(input())
ans = []
for _ in range(t):
    ans.append(sum(list(map(int, input().split(',')))))
for a in ans:
    print(a)