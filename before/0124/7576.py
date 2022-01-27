from collections import deque

n, m = list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph):
    queue = deque([])
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                queue.extend([x, y])

    while queue:
        current_x = queue.popleft()
        current_y = queue.popleft()
        for i in range(4):
            new_x = current_x + dx[i]
            new_y = current_y + dy[i]
            if new_x not in range(m) or new_y not in range(n):
                continue
            if graph[new_x][new_y] == 0:
                graph[new_x][new_y] = graph[current_x][current_y] + 1
                queue.extend([new_x, new_y])
    
    for g in graph:
        if 0 in g:
            return -1
    return max(list(map(max, graph))) - 1
        


tomatoes = [[] for _ in range(m)]
for i in range(m):
    tomatoes[i] = list(map(int, input().split()))

print(bfs(tomatoes))