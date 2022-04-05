import sys
def sol(graph, x, y, d, g):
    #일단 0세대만 만들기
    gen0 = []
    gen0.append(d)
    res = gen0[:]
    for i in range(1, g+1):
        tempGen = res[:]
        while tempGen:
            res.append((tempGen.pop()+1)%4)

    graph[y][x] = 1
    for i in res:
        x, y = x + dir[i][0], y + dir[i][1]
        graph[y][x] = 1

N = int(sys.stdin.readline().rstrip())
graph = [[0]*101 for i in range(101)]
dir = [(1,0), (0,-1), (-1,0), (0,1)] # → ↑ ← ↓
for i in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    sol(graph, x, y, d, g)

#findSquare
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            ans += 1
print(ans)


