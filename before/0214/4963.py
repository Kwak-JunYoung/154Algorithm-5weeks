import sys

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def find_unvisited(graph):
    j = len(graph)
    i = len(graph[0])

    for x in range(i):
        for y in range(j):
            if graph[y][x] == 1:
                return x, y
    return -1, -1

ans_arr = []

while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    if [w, h] == [0, 0]:
        break

    zido = [[] for _ in range(h)]
    for i in range(h):
        zido[i] = list(map(int, sys.stdin.readline().split()))
    
    dummy = 0
    while True:
        start_x, start_y = find_unvisited(zido)
        if [start_x, start_y] == [-1, -1]:
            break
        stack = [(start_x, start_y)]

        while stack:
            cur_x, cur_y = stack.pop()
            zido[cur_y][cur_x] = 0

            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x in range(w) and next_y in range(h) and zido[next_y][next_x] != 0:
                    stack.append((next_x, next_y))

        dummy += 1
    ans_arr.append(dummy)
        
for ans in ans_arr:
    print(ans)