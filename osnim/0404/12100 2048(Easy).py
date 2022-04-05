def move(arr, i):
    # 위로 이동
    if i == 0:
        for y in range(N):
            for x in range(1, N - 1):
                if arr[x][y] == arr[x + 1][y]:
                    arr[x][y] = arr[x][y] + arr[x + 1][y]
                    arr[x + 1][y] = 0
                elif arr[x][y] == 0:
                    arr[x][y] = arr[x + 1][y]
                    arr[x + 1][y] = 0
    # 아래로 이동
    elif i == 1:
        for y in range(N):
            for x in range(N - 1, 0, -1):
                # 아래로 이동
                if arr[x][y] == arr[x - 1][y]:
                    arr[x][y] = arr[x][y] + arr[x - 1][y]
                    arr[x - 1][y] = 0
                elif arr[x][y] == 0:
                    arr[x][y] = arr[x - 1][y]
                    arr[x - 1][y] = 0
    # 왼쪽으로 이동
    elif i == 2:
        for x in range(N):
            for y in range(N - 1):
                if arr[x][y] == arr[x][y + 1]:
                    arr[x][y] = arr[x][y] + arr[x][y + 1]
                    arr[x][y + 1] = 0
                elif arr[x][y] == 0:
                    arr[x][y] = arr[x][y + 1]
                    arr[x][y + 1] = 0
    # 오른쪽으로 이동
    elif i == 3:
        for x in range(N):
            for y in range(N - 1, 0, -1):
                if arr[x][y] == arr[x][y - 1]:
                    arr[x][y] = arr[x][y] + arr[x][y - 1]
                    arr[x][y - 1] = 0
                elif arr[x][y] == 0:
                    arr[x][y] = arr[x][y - 1]
                    arr[x][y - 1] = 0

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

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dfs(graph, 0)
print(ans)