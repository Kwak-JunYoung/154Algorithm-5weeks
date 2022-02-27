import sys
n = int(sys.stdin.readline())
ans = []
for _ in range(n):
    ans.append(int(sys.stdin.readline()))
ans.sort()
for i in range(n):
    print(ans[i])
