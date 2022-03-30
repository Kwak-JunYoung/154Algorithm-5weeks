import sys
from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if visited[i] == False:
            DFS(graph, i, visited)

def BFS(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
       v = queue.popleft()
       print(v, end=" ")

       for i in graph[v]:
           if not visited[i]:
               queue.append(i)
               visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0, 0]] + [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[x].sort()
    graph[y].append(x)
    graph[y].sort()


visited = [True] + [False]*(N)
DFS(graph, V, visited)
print()

visited = [True] + [False]*(N)
BFS(graph, V, visited)