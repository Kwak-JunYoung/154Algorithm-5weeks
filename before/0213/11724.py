import sys
n, m = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
ans = 0

visited = [False] * (n + 1)
visited[0] = True
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

while False in visited:
    i = visited.index(False)
    stack = [i]
    visited[i] = True
    while stack:
        cur = stack.pop()
        visited[cur] = True
        for x in graph[cur]:
            if visited[x] == False:
                stack.append(x)
    ans += 1

print(ans)