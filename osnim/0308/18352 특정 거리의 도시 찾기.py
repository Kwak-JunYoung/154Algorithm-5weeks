import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(300000+1)]
visited = [False]*(300000+1)
dist = [0]*(300000+1)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

#for i in range(M):
    #graph[i].sort()

def BFS(graph, x, visited, dist):
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()
        #print(v)

        for i in graph[v]:
            if not visited[i]:
                dist[i] = dist[v] + 1
                queue.append(i)
                visited[i] = True

BFS(graph, X, visited, dist)
#print(graph)
#print(dist)

if K not in dist:
    print(-1)

else:
    for i in range(1, 300000+1):
        if dist[i] == K:
            print(i)



