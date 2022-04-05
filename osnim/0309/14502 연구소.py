import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().split())

# 벽 세우고 virus가 퍼진 후 그래프
def virus_BFS(x, y, tempGraph):
    queue = deque()
    queue.append([x, y])
    tempGraph[x][y] = 2
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny <M:
                if tempGraph[nx][ny] == 0:
                    tempGraph[nx][ny] = 2
                    queue.append([nx, ny])

    return tempGraph

graph = []
zeroLocate = [] #0의 좌표를 저장한 리스트
virusLocate = [] # 바이러스의 위치를 저장한 리스트
virusGraph = [] # 바이러스가 퍼진 그래프
tempGraph = [] # 그래프의 내용을 변경하기 위한 임시 그래프
combinationsZeroLocate = [] #0의 좌표 중 3개 뽑는 경우의 수를 저장한 리스트
result = 0 # 최종 안전 영역

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if graph[i][j] == 0:
            zeroLocate.append([i, j])
        elif graph[i][j] == 2:
            virusLocate.append([i, j])

#virusGraph = copy.deepcopy(graph)
virusGraph = [i[:] for i in graph]
combinationsZeroLocate = (list(combinations(zeroLocate, 3)))

for i in combinationsZeroLocate:
    temp = 0
    tempGraph = copy.deepcopy(graph)

    tempGraph[i[0][0]][i[0][1]] = 1
    tempGraph[i[1][0]][i[1][1]] = 1
    tempGraph[i[2][0]][i[2][1]] = 1

    for j in virusLocate:
        #virusGraph = copy.deepcopy(virus_BFS(j[0], j[1], tempGraph))
        virusGraph = [i[:] for i in virus_BFS(j[0], j[1], tempGraph)]

    for j in virusGraph:
        temp += j.count(0)

    result = max(temp, result)

print(result)