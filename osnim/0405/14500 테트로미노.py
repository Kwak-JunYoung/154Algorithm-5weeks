def check(tetro):
    x1, y1, x2, y2, x3, y3, x4, y4 = tetro
    result = 0
    for i in range(N):
        for j in range(M):
            nx1, ny1, nx2, ny2, nx3, ny3, nx4, ny4 = x1 + i, y1 + j, x2 + i, y2 + j, x3 + i, y3 + j, x4 + i, y4 + j
            if 0 <= nx1 < N and 0 <= nx2 < N and 0 <= nx3 < N and 0 <= nx4 < N and 0 <= ny1 < M and 0 <= ny2 < M and 0 <= ny3 < M and 0 <= ny4 < M:
               temp = graph[nx1][ny1] + graph[nx2][ny2] + graph[nx3][ny3] + graph[nx4][ny4]
               result = max(temp, result)
    return result

N, M = map(int, input().split())
graph = []
ans = 0
temp_ans = 0
for i in range(N):
    graph.append(list(map(int, input().split())))

tetro1 = [0, 0, 0, 1, 0, 2, 0, 3]
tetro2 = [0, 0, 0, 1, 1, 0, 1, 1]
tetro3 = [0, 0, 1, 0, 2, 0, 2, 1]
tetro4 = [0, 0, 1, 0, 1, 1, 2, 1]
tetro5 = [0, 0, 0, 1, 0, 2, 1, 1]

temp_ans = check(tetro1)
ans = max(ans, temp_ans)

tetro1Rotate = [0, 0, 1, 0, 2, 0, 3, 0]
temp_ans = check(tetro1Rotate)
ans = max(ans, temp_ans)

temp_ans = check(tetro2)
ans = max(ans, temp_ans)

temp_ans = check(tetro3)
ans = max(ans, temp_ans)
tetro3Rotate1 = [0, 0, 0, 1, 0, 2, 1, 0]
temp_ans = check(tetro3Rotate1)
ans = max(ans, temp_ans)
tetro3Rotate2 = [0, 0, 0, 1, 1, 1, 2, 1]
temp_ans = check(tetro3Rotate2)
ans = max(ans, temp_ans)
tetro3Rotate3 = [1, 0, 1, 1, 1, 2, 0, 2]
temp_ans = check(tetro3Rotate3)
ans = max(ans, temp_ans)

tetro3symmetric1 = [0, 1, 1, 1, 2, 1, 2, 0]
temp_ans = check(tetro3symmetric1)
ans = max(ans, temp_ans)
tetro3symmetric2 = [0, 0, 1, 0, 1, 1, 1, 2]
temp_ans = check(tetro3symmetric2)
ans = max(ans, temp_ans)
tetro3symmetric3 = [0, 0, 0, 1, 1, 0, 2, 0]
temp_ans = check(tetro3symmetric3)
ans = max(ans, temp_ans)
tetro3symmetric4 = [0, 0, 0, 1, 0, 2, 1, 2]
temp_ans = check(tetro3symmetric4)
ans = max(ans, temp_ans)

temp_ans = check(tetro4)
ans = max(ans, temp_ans)
tetro4Rortate = [0, 1, 0, 2, 1, 0, 1, 1]
temp_ans = check(tetro4Rortate)
ans = max(ans, temp_ans)

tetro4symmetric1 = [0, 0, 0, 1, 1, 1, 1, 2]
temp_ans = check(tetro4symmetric1)
ans = max(ans, temp_ans)
tetro4symmetric1 = [0, 1, 1, 1, 1, 0, 2, 0]
temp_ans = check(tetro4symmetric1)
ans = max(ans, temp_ans)

temp_ans = check(tetro5)
ans = max(ans, temp_ans)
tetro5Rortate1 = [1, 0, 0, 1, 1, 1, 2, 1]
temp_ans = check(tetro5Rortate1)
ans = max(ans, temp_ans)
tetro5Rortate2 = [0, 1, 1, 0, 1, 1, 1, 2]
temp_ans = check(tetro5Rortate2)
ans = max(ans, temp_ans)
tetro5Rortate3 = [0, 0, 1, 0, 2, 0, 1, 1]
temp_ans = check(tetro5Rortate3)
ans = max(ans, temp_ans)

print(ans)
