import sys
from itertools import combinations
from collections import deque

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
storesCombs = [0]*(len(stores))

ans = int(10e9)
for i in stores:
    tempAns = 0
    for j in houses:
        hx, hy = j[0], j[1]
        shortDis = int(10e9)
        for k in i:
            sx, sy = k[0], k[1]
            dis = abs(hx - sx) + abs(hy - sy)
            shortDis = min(shortDis, dis)
        tempAns += shortDis

    ans = min(ans, tempAns)
print(ans)
#storesCombs.append(tempAns)



