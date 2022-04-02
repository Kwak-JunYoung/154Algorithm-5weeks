import sys

N = int(sys.stdin.readline())
graph = []
area = []
global house # 단지 수

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if graph[x][y] == 1:
        #해당노드 방문처리
        graph[x][y] = 0
        #집의 수
        global house
        house += 1
        #상 하 좌 우
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True

    return False

result = 0
house = 0
for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            result += 1
            area.append(house)
            house = 0

print(result)
area.sort()
for i in range(result):
    print(area[i])