import sys
from collections import deque

def BFS(virus, a, b, s):
    #for i in range(len(virusPositions[virus])):
    for j in range(4):
        nx = a + dx[j]
        ny = b + dy[j]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if virusGraph[nx][ny] == 0:
                virusGraph[nx][ny] = virus
                virusPositions.append([virus, nx, ny, s+1])

virusGraph = []

N, K = map(int, sys.stdin.readline().split())
for i in range(N):
    virusGraph.append(list(map(int, sys.stdin.readline().split())))

virusPositions = []

for i in range(N):
    for j in range(N):
        if virusGraph[i][j] != 0:
            #바이러스 번호, 바이러스 좌표, 시간
            virusPositions.append([virusGraph[i][j], i, j, 0])

#print(virusPositions)
virusPositions.sort(key=lambda x: x[0])
#print(virusPositions)
virusPositions = deque(virusPositions)

S, X, Y = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#S초만큼만 반복 => 이렇게 하면 10 초가 넘어가면 pop이 비어있음
while virusPositions:
    if virusGraph[X-1][Y-1] != 0:
        break

    #for i in range(N):
        #print(virusGraph[i])

    virusNum, x, y, s = virusPositions.popleft()
    if s == S:
        break
    #print(virusNum, x, y, s)
    BFS(virusNum, x, y, s)

print(virusGraph[X-1][Y-1])

