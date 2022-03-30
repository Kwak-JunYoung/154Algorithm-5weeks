import sys
def findFish(MAP, idx):
    for i in range(4):
        for j in range(4):
            if MAP[i][j][0] == -1:
                continue
            if MAP[i][j][0] == idx:
                return [i, j]
    return False

def food(MAP, x, y):  # 상어가 먹을 수 있는 후보 위치 반환
    positions = []
    direction = MAP[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= MAP[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions

def fishRotate(sx, sy, MAP):
    # 물고기 회전, 번호 낮은  순서

    for k in range(1, 17):
        result = findFish(MAP, k)
        if result:
            # findFish(MAP):
            i, j = result[0], result[1]
            if i == sx and j == sy: continue
            if MAP[i][j][0] == -1: continue
            fishNum, fishDir = MAP[i][j]

            for k in range(8):
                x, y = i + dx[(fishDir) % 8], j + dy[(fishDir) % 8]
                if x == sx and y == sy:
                    continue
                if 0 <= x < 4 and 0 <= y < 4:
                    # findFish(fishList, k[0])
                    # fishList도 교환
                    tempFishNum, tempFishDir = MAP[x][y]
                    MAP[x][y] = MAP[i][j]
                    MAP[i][j] = [tempFishNum, tempFishDir]

                    break
                fishDir += 1
        return MAP

def ffindFish(x, y, MAP):
    if MAP[x][y][0] != -1:
        return True
    return False

def DFS(sx, sy, MAP, ans, level):
    # 물고기 체크
    global total
    MAP = [i[:] for i in MAP]
    num, sDir = MAP[sx][sy][0], MAP[sx][sy][1]  # 번호와 방향
    ans += num
    total = max(total, ans)
    print(sx, sy)
    MAP[sx][sy] = [-1, -1]

    # 물고기 회전
    MAP = fishRotate(sx, sy, MAP)
    # 먹을 물고기가 있는지 확인
    result = food(MAP, sx, sy)

    for x, y in result:
        DFS(x, y, MAP, ans, level+1)

temp = []
MAP = [[[0, 0]]*4 for i in range(4)]
total = 0

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(4):
    temp.append(list(map(int, sys.stdin.readline().split())))

for i in range(4):
    k = 0
    for j in range(0, 8, 2):
        MAP[i][k] = [temp[i][j], (temp[i][j+1])-1]
        #fishList.append([temp[i][j], i, k, (temp[i][j+1])-1])
        k += 1
#fishList.sort()
DFS(0, 0, MAP, 0, 0)
print(total)

