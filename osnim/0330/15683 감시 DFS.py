import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
office = []
cctvList = []


def checkTop(i, j, tempOff):
    result = 0
    if i < 0: return result  # 사무실 바깥일때
    for k in range(i, -1, -1):
        if tempOff[k][j] == 6:
            return  # 벽
        elif tempOff[k][j] != 0:
            continue  # 다른 cctv
        else:
            tempOff[k][j] = -1
    return result, tempOff


def checkBottom(i, j, tempOff):
    result = 0
    if i > N: return result
    for k in range(i, N):
        if tempOff[k][j] == 6:  # 벽
            return
        elif tempOff[k][j] != 0:  # 다른 cctv
            continue
        else:
            tempOff[k][j] = -1
    return result, tempOff


def checkRight(i, j, tempOff):
    result = 0
    if j > M: return result
    for k in range(j, M):
        if tempOff[i][k] == 6:  # 벽
            return
        elif tempOff[i][k] != 0:  # 다른 cctv
            continue
        else:
            tempOff[i][k] = -1
    return result, tempOff


def checkLeft(i, j, tempOff):
    result = 0
    if j < 0: return result  # 사무실 바깥일때
    for k in range(j, -1, -1):
        if tempOff[i][k] == 6:  # 벽
            return
        elif tempOff[i][k] != 0:  # 다른 cctv
            continue
        else:
            tempOff[i][k] = -1
    return result, tempOff


def sol(cctvList):
    num, i, j = cctvList.pop(0)
    ans = 0
    if num == 5:
        ans += checkTop(i - 1, j, office) + checkBottom(i + 1, j, office) + checkRight(i, j + 1, office) + checkLeft(i, j - 1)
    elif num == 4:
        tempAns1, tempAns2, tempAns3, tempAns4 = 0, 0, 0, 0
        officeList = []
        tempOff1 = [i[:] for i in office]
        tempOff2 = [i[:] for i in office]
        tempOff3 = [i[:] for i in office]
        tempOff4 = [i[:] for i in office]

        officeList.append(
            checkTop(i - 1, j, tempOff1) + checkRight(i, j + 1, tempOff1) + checkBottom(i + 1, j, tempOff1))
        officeList.append(
            checkRight(i, j + 1, tempOff2) + checkBottom(i + 1, j, tempOff2) + checkLeft(i, j - 1, tempOff2))
        officeList.append(
            checkBottom(i + 1, j, tempOff3) + checkLeft(i, j - 1, tempOff3) + checkTop(i - 1, j, tempOff3))
        officeList.append(checkLeft(i, j - 1, tempOff4) + checkTop(i - 1, j, tempOff4) + checkRight(i, j + 1, tempOff4))

        officeList.sort(key=lambda x: (-x[0]))

        ans += officeList[0][1]

    elif num == 3:
    elif num == 2:
    elif num == 1:

    return

def cctv5(i, j):
    result = checkTop(i - 1, j) + checkBottom(i + 1, j) + checkRight(i, j + 1) + checkLeft(i, j - 1)
    return result

def cctv4(i, j, office, dList):
    for d in dList
        result = checkTop(i - 1, j, office) + checkBottom(i + 1, j, office) + checkRight(i, j + 1, office) + checkLeft(i, j - 1, office)


    return result

def dfs(i, j, office, dList):


    return

dir = [0,1,2,3] # 북, 동, 남, 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
zero = 0
for i in range(N):
    for j in range(M):
        office[i].append(list(map(int, sys.stdin.readline().split())))
        if 0 < office[i][j] < 6:
            cctvList.append([office[i][j], i, j])
        if office[i][j] == 0:
            zero += 1

cctvList.sort(key=lambda x: (-x[0]))
print(cctvList)
for cctv in cctvList:
    ans = 0
    if cctv[0] == 5:
       ans += dfs(cctv[1], cctv[2])
    elif cctv[0] == 4:
        cctv4(cctv[1], cctv[2], office, dir)




