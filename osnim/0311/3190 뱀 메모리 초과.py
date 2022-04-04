import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # N x N
K = int(sys.stdin.readline().rstrip()) # 사과 개수

apples = [] #사과 좌표
snakeHead = [0, 0, 0]
snakeBody = [] #뱀의 몸통 좌표

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    apples.append([x-1, y-1])

L = int(sys.stdin.readline().rstrip()) # 뱀의 방향 변환 횟수
turnings = []

#동, 남, 서, 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
directions = [0, 1, 2, 3]

for i in range(L):
    X, C = sys.stdin.readline().split()
    turnings.append([int(X), C])

def turn_right():
    snakeHead[2] += 1
    if snakeHead[2] > 3:
        snakeHead[2] = 0

def turn_left():
    snakeHead[2] -= 1
    if snakeHead[2] < 0:
        snakeHead[2] = 3

def checkBodyCrush():
    for i in snakeBody:
        if snakeHead[0] == i[0] and snakeHead[1] == i[1]:
            return True
time = 0
while True:
    # 이동
    time += 1

    if turnings:
        X, C = turnings[0]
        if time == X:
            if C == "D":
                turn_right()
            else:
                turn_left()
            turnings.pop(0)
            continue

    for i in range(4):
        if snakeHead[2] == directions[i]:
            snakeHead[0] = snakeHead[0]+dx[i]
            snakeHead[1] = snakeHead[1]+dy[i]

            for k in range(len(snakeBody)):
                snakeBody.append([snakeBody[k][0] + dx[i], snakeBody[k][1] + dy[i]])

            # 사과가 있을 경우
            if apples:
                for j in range(len(apples)):
                    if snakeHead[0] == apples[j][0] and snakeHead[1] == apples[j][1]:
                        snakeBody.append([snakeHead[0] - dx[i], snakeHead[1] - dy[i]])
                        apples.pop(j)
                        break

    ## 밖에 나간 경우
    if snakeHead[0] < 0 or snakeHead[0] >= N or snakeHead[1] < 0 or snakeHead[1] >= N:
        print(time)
        break

    #자신의 몸에 부딪힌 경우 체크
    if checkBodyCrush():
        print(time-1)
        break


