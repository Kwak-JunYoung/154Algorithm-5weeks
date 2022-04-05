def dfs(tempArr, up, down, left, right, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, tempArr[i][j])
        return

    if up:
        arr = [i[:] for i in tempArr]
        for y in range(N):
            top = 0
            for x in range(1, N):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[top][y] == arr:
                        arr[top][y] = arr[top][y] + temp
                        top += 1
                    elif arr[top][y] == 0:
                        arr[top][y] = temp
                    else:
                        top += 1
                        arr[top][y] = temp  #
        dfs(arr, up-1, down, left, right, cnt+1)


    elif down:
        arr = [i[:] for i in tempArr]
        # 아래로 이동
        for y in range(N):
            bot = N - 1
            for x in range(N - 2, -1, ):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[bot][y] == temp:
                        arr[bot][y] = arr[bot][y] + temp
                        bot -= 1
                    elif arr[bot][y] == 0:
                        arr[bot][y] = temp
                    else:
                        bot += 1
                        arr[bot][y] = temp  #

        dfs(arr, up, down-1, left, right, cnt + 1)


    elif left:
        arr = [i[:] for i in tempArr]
        for x in range(N):
            left = 0
            for y in range(1, N):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[x][left] == temp:
                        arr[x][left] = arr[x][left] + temp
                        left += 1
                    elif arr[x][left] == 0:
                        arr[x][left] = temp
                    else:
                        left += 1
                        arr[x][left] = temp  #
        dfs(arr, up, down, left-1, right, cnt + 1)

    elif right:
        arr = [i[:] for i in tempArr]
        for x in range(N):
            right = N - 1
            for y in range(N - 2, -1, ):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[x][right] == temp:
                        arr[x][right] = arr[x][right] + temp
                        right -= 1
                    elif arr[x][right] == 0:
                        arr[x][right] = temp
                    else:
                        right += 1
                        arr[x][right] = temp  #

        dfs(arr, up, down, left, right-1, cnt + 1)


N = int(input())
graph = []
ans = -1
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


dfs(graph, 5, 5, 5, 5, 0)
print(ans)