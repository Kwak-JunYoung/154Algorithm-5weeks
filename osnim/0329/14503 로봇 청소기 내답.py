import sys
from collections import deque
def checkLeft(nx, ny):
    if MAP[nx][ny] == 0:
        if 1 <= nx < N - 1 and 1 <= ny < M - 1:
            return True
    else:
        return False

def checkGoBack(x, y, d, MAP):
    nd = (d + 2) % 4 # 뒤로 가기
    nx, ny = x + dx[nd], y + dy[nd]
    if MAP[nx][ny] == 1:
        return False
    return nx, ny

def BFS(r, c, direction, MAP):
    cnt = 2
    q = deque()
    q.append([r, c, direction])

    while q:
        x, y, d = q.popleft()
        MAP[x][y] = cnt
        nd = d
        for i in range(4):
            nd -= 1
            if nd == -1: nd = 3
            nx, ny = x + dx[nd], y + dy[nd]
            if checkLeft(nx, ny):
                 cnt += 1
                 q.append((nx, ny, nd))
                 break

            # 4방향 모두 확인했는데 청소할 공간이 없는 경우
            elif i == 3:
                result = checkGoBack(x, y, d, MAP)
                if not result:
                    return cnt - 1

                else:
                    nx, ny = result
                    q.append((nx, ny, d))  # 방향은 그대로

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, sys.stdin.readline().split())))

#회전:북 > 서 > 남 > 동 = 0 > 3 > 2 > 1
# 북동남서 방향으로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(BFS(r, c, d, MAP))

