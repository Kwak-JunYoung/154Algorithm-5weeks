import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    orders = input().split()
    up = [['w' for _ in range(3)] for _ in range(3)]
    down = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]
    for order in orders:
        side, turn = order[0], order[1]
        if side == 'U':
            if turn == '+':
                up[0][0], up[0][1], up[0][2], up[1][2], up[2][2], up[2][1], up[2][0], up[1][0] = up[2][0], up[1][0], \
                                                                                                 up[0][0], up[0][1], \
                                                                                                 up[0][2], up[1][2], \
                                                                                                 up[2][2], up[2][1]
                front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], \
                back[0][2], left[0][0], left[0][1], left[0][2] = right[0][0], right[0][1], right[0][2], back[0][0], \
                                                                 back[0][1], back[0][2], left[0][0], left[0][1], \
                                                                 left[0][2], front[0][0], front[0][1], front[0][2]
            else:
                up[0][0], up[0][1], up[0][2], up[1][2], up[2][2], up[2][1], up[2][0], up[1][0] = up[0][2], up[1][2], \
                                                                                                 up[2][2], up[2][1], \
                                                                                                 up[2][0], up[1][0], \
                                                                                                 up[0][0], up[0][1]
                front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], \
                back[0][2], left[0][0], left[0][1], left[0][2] = left[0][0], left[0][1], left[0][2], front[0][0], \
                                                                 front[0][1], front[0][2], right[0][0], right[0][1], \
                                                                 right[0][2], back[0][0], back[0][1], back[0][2]
        if side == 'D':
            if turn == '+':
                down[0][0], down[0][1], down[0][2], down[1][2], down[2][2], down[2][1], down[2][0], down[1][0] = \
                down[2][0], down[1][0], down[0][0], down[0][1], down[0][2], down[1][2], down[2][2], down[2][1]
                front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], \
                back[2][2], left[2][0], left[2][1], left[2][2] = left[2][0], left[2][1], left[2][2], front[2][0], \
                                                                 front[2][1], front[2][2], right[2][0], right[2][1], \
                                                                 right[2][2], back[2][0], back[2][1], back[2][2]
            else:
                down[0][0], down[0][1], down[0][2], down[1][2], down[2][2], down[2][1], down[2][0], down[1][0] = \
                down[0][2], down[1][2], down[2][2], down[2][1], down[2][0], down[1][0], down[0][0], down[0][1]
                front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], \
                back[2][2], left[2][0], left[2][1], left[2][2] = right[2][0], right[2][1], right[2][2], back[2][0], \
                                                                 back[2][1], back[2][2], left[2][0], left[2][1], \
                                                                 left[2][2], front[2][0], front[2][1], front[2][2]
        if side == 'F':
            if turn == '+':
                front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0] = \
                front[2][0], front[1][0], front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1]
                right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], \
                down[2][0], down[2][1], down[2][2] = up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], \
                                                     down[2][0], down[2][1], down[2][2], right[0][0], right[1][0], \
                                                     right[2][0]
            else:
                front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0] = \
                front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0], front[0][0], front[0][1]
                right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], \
                down[2][0], down[2][1], down[2][2] = down[2][0], down[2][1], down[2][2], right[0][0], right[1][0], \
                                                     right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], \
                                                     left[0][2]
        if side == 'B':
            if turn == '+':
                back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0] = \
                back[2][0], back[1][0], back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1]
                up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], \
                left[2][0], left[1][0], left[0][0] = right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], \
                                                     down[0][2], left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], \
                                                     up[0][2]
            else:
                back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0] = \
                back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0], back[0][0], back[0][1]
                right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], \
                left[0][0], up[0][0], up[0][1], up[0][2] = up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], \
                                                           right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], \
                                                           left[1][0], left[0][0]
        if side == 'L':
            if turn == '+':
                left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0] = \
                left[2][0], left[1][0], left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1]
                front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], \
                back[0][2], up[0][0], up[1][0], up[2][0] = up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], \
                                                           front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], \
                                                           back[1][2], back[0][2]
            else:
                left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0] = \
                left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0], left[0][0], left[0][1]
                up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], \
                back[2][2], back[1][2], back[0][2] = front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], \
                                                     down[0][2], back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], \
                                                     up[2][0]
        if side == 'R':
            if turn == '+':
                right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0] = \
                right[2][0], right[1][0], right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1]
                up[0][2], up[1][2], up[2][2], front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], down[0][0], \
                back[2][0], back[1][0], back[0][0] = front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], \
                                                     down[0][0], back[2][0], back[1][0], back[0][0], up[0][2], up[1][2], \
                                                     up[2][2]
            else:
                right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0] = \
                right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0], right[0][0], right[0][1]
                front[0][2], front[1][2], front[2][2], up[0][2], up[1][2], up[2][2], back[2][0], back[1][0], back[0][0], \
                down[2][0], down[1][0], down[0][0] = up[0][2], up[1][2], up[2][2], back[2][0], back[1][0], back[0][0], \
                                                     down[2][0], down[1][0], down[0][0], front[0][2], front[1][2], \
                                                     front[2][2]
    for i in up:
        print(''.join(i))