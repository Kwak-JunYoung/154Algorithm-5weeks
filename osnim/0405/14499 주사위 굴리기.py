def check(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False
N, M, x, y, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
commands = list((map(int, input().split())))
dice = [0, 0, 0, 0, 0, 0, 0]

for cmd in commands:
    if cmd == 1: # 동
        nx, ny = x, y + 1
        if check(nx, ny):
            dice1, dice2, dice3, dice4, dice5, dice6 = dice[1], dice[2],  dice[3], dice[4], dice[5], dice[6]
            dice[1], dice[2],  dice[3], dice[4], dice[5], dice[6]  = dice4, dice2, dice1, dice6, dice5, dice3
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[6]
            else:
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice[1])
        else:
            continue

    elif cmd == 2: # 서
        nx, ny = x, y - 1
        if check(nx, ny):
            dice1, dice2, dice3, dice4, dice5, dice6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice3, dice2, dice6, dice1, dice5, dice4
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[6]
            else:
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice[1])
        else:
            continue

    elif cmd == 3: # 북
        nx, ny = x - 1, y
        if check(nx, ny):
            dice1, dice2, dice3, dice4, dice5, dice6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice5, dice1, dice3, dice4, dice6, dice2
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[6]
            else:
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice[1])
        else:
            continue

    else: # 남
        nx, ny = x + 1, y
        if check(nx, ny):
            dice1, dice2, dice3, dice4, dice5, dice6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
            dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice2, dice6, dice3, dice4, dice1, dice5
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[6]
            else:
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice[1])
        else:
            continue

    x, y = nx, ny
