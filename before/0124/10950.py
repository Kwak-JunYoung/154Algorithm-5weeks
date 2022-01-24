n = int(input())
ans = []
for i in range(n):
    a, b = list(map(int, input().split()))
    ans.append(a + b)
for a in ans:
    print(a)
