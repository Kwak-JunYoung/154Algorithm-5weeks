def move(arr, i):
    # 위로 이동 #한 칸씩 가는 게 아니라 0 안 만날 때까지
    if i == 0:
        for y in range(N):
            top = 0
            for x in range(1, N):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[top][y] == temp:
                        arr[top][y] = arr[top][y] + temp
                        top += 1
                    elif arr[top][y] == 0:
                        arr[top][y] = temp
                    else:
                        top += 1
                        arr[top][y] = temp #
    # 아래로 이동
    elif i == 1:
        for y in range(N):
            bot = N-1
            for x in range(N-2, -1, -1):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[bot][y] == temp:
                        arr[bot][y] = arr[bot][y] + temp
                        bot -= 1
                    elif arr[bot][y] == 0:
                        arr[bot][y] = temp
                    else:
                        bot -= 1
                        arr[bot][y] = temp  #
    # 왼쪽으로 이동
    elif i == 2:
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
    # 오른쪽으로 이동
    elif i == 3:
        for x in range(N):
            right = N - 1
            for y in range(N - 2, -1, -1):
                if arr[x][y]:
                    temp = arr[x][y]
                    arr[x][y] = 0
                    if arr[x][right] == temp:
                        arr[x][right] = arr[x][right] + temp
                        right -= 1
                    elif arr[x][right] == 0:
                        arr[x][right] = temp
                    else:
                        right -= 1
                        arr[x][right] = temp  #
    return arr

def dfs(arr, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
               ans = max(ans, arr[i][j])
        return

    for i in range(4):
        tempArr = [i[:] for i in arr]
        tempArr = move(tempArr, i)
        dfs(tempArr, cnt+1)

N = int(input())
graph = []
ans = -1
for i in range(N):
    graph.append(list(map(int, input().split())))

dfs(graph, 0)
print(ans)