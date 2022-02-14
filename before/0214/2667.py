import sys
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans_arr = []

aparts = [[] for _ in range(n)]
for i in range(n):
    aparts[i] = list(map(int, input()))

def find_unvisited():
    for i in range(n):
        for j in range(n):
            if aparts[i][j] == 1:
                return i, j
    return -1, -1


while True:
    start_x, start_y = find_unvisited()
    if [start_x, start_y] == [-1, -1]:
        break

    stack = [(start_x, start_y)]
    aparts[start_x][start_y] = 0
    dummy = 0
    while stack:
        cur_x, cur_y = stack.pop()
        dummy += 1
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x in range(n) and next_y in range(n) and aparts[next_x][next_y] == 1:
                stack.append((next_x, next_y))
                aparts[next_x][next_y] = 0

    ans_arr.append(dummy)

print(len(ans_arr))

for a in sorted(ans_arr):
    print(a)