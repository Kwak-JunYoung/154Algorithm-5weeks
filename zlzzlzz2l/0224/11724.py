import sys
sys.setrecursionlimit(10 ** 6) # python에서는 재귀의 깊이가 1000으로 제한되어 있어서 이거 depth를 늘려준다
input = sys.stdin.readline
N, M = map(int, input().split())

nums = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: x-1, map(int, input().split()))
    nums[u][v] = nums[v][u] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if nums[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)