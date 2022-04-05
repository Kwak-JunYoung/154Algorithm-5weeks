import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)

visited = [False] * (n + 1)
q = deque()

q.append((x, 0))
visited[x] = True

result = []
while q:
    popped, dist = q.popleft()

    if dist == k:
        result.append(popped)
        continue

    for neighbor in graph[popped]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append((neighbor, dist + 1))

if len(result) == 0:
    print(-1)
else:
    for node in sorted(result):
        print(node)
