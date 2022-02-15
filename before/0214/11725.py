import sys

n = int(input())

graph = [[] for _ in range(n + 1)]

parent = {}
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited[0] = True
while stack:
    cur = stack.pop()
    visited[cur] = True

    for x in graph[cur]:
        if visited[x] == False:
            parent[x] = cur
            stack.append(x)

for i in range(2, n + 1):
    print(parent[i])