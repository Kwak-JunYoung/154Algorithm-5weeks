import sys
from itertools import combinations
from collections import deque

def BFS(store, hx, hy):
    visited = [[False] * N for i in range(N)]
    q = []
    q = deque(q)
    q.append([hx, hy])
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                for j in store:
                    sx, sy = j[0], j[1]
                    if nx == sx and ny == sy:  # 가장 가까운 치킨 집
                        result = abs(hx - sx) + abs(hy - sy)
                        return result

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

N, M = map(int, sys.stdin.readline().split())
graph = []
houses = []
temp = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j] == 1:
            houses.append([i, j])
        elif graph[i][j] == 2:
            temp.append([i, j])

stores = deque(combinations(temp, M))

ans = int(10e9)
for i in stores:
    tempAns = 0
    #tempHouses = deque(i[:] for i in houses)
    for j in houses:
    #while tempHouses:
        hx, hy = j[0], j[1]
        temp = BFS(i, hx, hy)
        tempAns = tempAns + temp
    ans = min(ans, tempAns)

print(ans)


