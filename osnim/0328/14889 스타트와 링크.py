import sys
from itertools import combinations
MAP = []
N = int(sys.stdin.readline())
MIN = int(1e9)
for i in range(N):
    MAP.append(list(map(int, sys.stdin.readline().split())))
star = []

def abilitySum(arr):
    result = 0
    comArr = combinations(arr, 2)
    for i in comArr:
        result += MAP[i[0]][i[1]] + MAP[i[1]][i[0]]
    return result

def dfs(start):
    global MIN
    if len(star) == N//2:
        starSum = abilitySum(star)
        link = []
        for i in range(N):
            if i not in star:
                link.append(i)
        linkSum = abilitySum(link)
        MIN = min(abs(starSum-linkSum), MIN)
        return

    for i in range(start, N):
        if i not in star:
            star.append(i)
            dfs(i+1)
            star.pop()
dfs(0)
print(MIN)