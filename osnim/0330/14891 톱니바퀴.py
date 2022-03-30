import sys
from collections import deque
def checkRight(idx, clockWise):
    if idx > 3 or gears[idx-1][2] == gears[idx][6]:
        return
    if gears[idx-1][2] != gears[idx][6]:
        checkRight(idx+1, -clockWise)
        gears[idx].rotate(clockWise)

def checkLeft(idx, clockWise):
    if idx < 0 or gears[idx][2] == gears[idx + 1][6]:
        return
    if gears[idx][2] != gears[idx + 1][6]:
        checkLeft(idx-1, -clockWise)
        gears[idx].rotate(clockWise)

gears = []
for i in range(4):
    gears.append(deque(list(sys.stdin.readline().rstrip())))

#시작
K = int(sys.stdin.readline())
for i in range(K):
    gear, clockWise = map(int, sys.stdin.readline().split())
    # 시계 1, 반시계 -1
    checkRight(gear, -clockWise)
    checkLeft(gear-2, -clockWise)
    gears[gear-1].rotate(clockWise)

result = 0
for i in range(4):
    if gears[i][0] == '1':
        result += (2**i)

print(result)