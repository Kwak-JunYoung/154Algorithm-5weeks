import sys
from collections import deque
# 구슬 굴리기 가능한지 판단
def promising(MAP, rx, ry, bx, by):
    for
    MAP[rx][ry]

    return result

def DFS(MAP, rx, ry, bx, by, cnt):
    redQ = deque([rx, ry])
    blueQ = deque([bx, by])
    while redQ and blueQ:
        rx, ry = redQ.popleft()
        bx, by = blueQ.popleft()

        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]

            if MAP[nrx][nry] == "O":
                answer = min(cnt, answer)
                return cnt

            elif MAP[nrx][nry] == "#" or MAP[nrx][nry] == "B":
                MAP[rx][ry] = "R"
                redQ.append([nrx, nry])
                continue

            else:




        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]


            if MAP[nrx][nry]


    global answer


    if promising(MAP, rx, ry, bx, by):

        DFS(MAP, rx, ry, bx, by, cnt)










    if cnt > 10:
        return False
    else:
        return result



N, M = map(int, sys.stdin.readline().split())
MAP = []
for i in range(N):
    MAP.append(list(sys.stdin.readline().rstrip()))

rx, ry, bx, by, ox, oy = 0, 0, 0, 0, 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'R':
            rx, ry = i, j
        if MAP[i][j] == 'B':
            bx, by = i, j
        if MAP[i][j] == 'O':
            ox, oy = i, j

answer = 0
result = DFS(MAP, rx, ry, bx, by, 0)
if not result:
    print(result)
else:
    print(-1)

