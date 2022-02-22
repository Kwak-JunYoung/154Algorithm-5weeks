import sys
from collections import deque

def bfs(graph, visited, count):
    queue = deque()
    for v in range(1, n+1):
        if visited[v] == False:
            queue.append(v)
            visited[v] = True

            while queue:
                v = queue.popleft()
                for i in range(2*m):
                    if graph[i][0] == v and visited[graph[i][1]] == False:
                        queue.append(graph[i][1])
                        visited[graph[i][1]] = True
            count += 1
        else: 
            continue
    return count

n, m = map(int, input().split())

count = 0
graph = []
visited = [False] * (n+1)


# 초기화
for i in range(2*m):
    graph.append([])
    for j in range(2):
        graph[i].append(0)

# 값 저장
for i in range(m):
    u , v = map(int, sys.stdin.readline().strip().split())
    graph[i][0] = u
    graph[i][1] = v

    # 양방향
    graph[2*m-1-i][0] = v
    graph[2*m-1-i][1] = u


count = bfs(graph,visited,count)
print(count)