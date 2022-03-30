import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
office = []
cctvList = []

def checkTop(i, j, tempOff):
    result = 0
    if i < 0: return result #사무실 바깥일때
    for k in range(i, -1, -1):
        if tempOff[k][j] == 6: return # 벽
        elif tempOff[k][j] != 0: continue #다른 cctv
        else:
            tempOff[k][j] = -1
            result += 1
    return [result, tempOff]

def checkBottom(i, j, tempOff):
    result = 0
    if i > N: return result
    for k in range(i, N):
        if tempOff[k][j] == 6: #벽
            return [result, tempOff]
        elif tempOff[k][j] != 0: #다른 cctv
            continue
        else:
            result += 1
            tempOff[k][j] = -1
    return [result, tempOff]

def checkRight(i, j, tempOff):
    result = 0
    if j > M: return result
    for k in range(j, M):
        if tempOff[i][k] == 6: #벽
            return [result, tempOff]
        elif tempOff[i][k] != 0: #다른 cctv
            continue
        else:
            result += 1
            tempOff[i][k] = -1
    return [result, tempOff]

def checkLeft(i, j, tempOff):
    result = 0
    if j < 0: return result  # 사무실 바깥일때
    for k in range(j, -1, -1):
        if tempOff[i][k] == 6: #벽
            return [result, tempOff]
        elif tempOff[i][k] != 0: #다른 cctv
            continue
        else:
            result += 1
            tempOff[i][k] = -1
    return [result, tempOff]

def sol(office, cctvList):
    num, i, j = cctvList.pop(0)
    ans = 0
    if num == 5:
        temp, office = checkTop(i-1, j, office) + checkBottom(i + 1, j, office) + checkRight(i, j + 1, office) + checkLeft(i, j - 1, office)
        ans += temp
    elif num == 4:
        officeList = []
        tempOff1 = [i[:] for i in office]
        tempOff2 = [i[:] for i in office]
        tempOff3 = [i[:] for i in office]
        tempOff4 = [i[:] for i in office]

        #officeList.append(checkTop(i - 1, j, tempOff1)+checkRight(i, j + 1, tempOff1)+checkBottom(i + 1, j, tempOff1))
        #officeList.append(checkRight(i, j + 1, tempOff2) + checkBottom(i + 1, j, tempOff2) + checkLeft(i, j - 1, tempOff2))
        #officeList.append(checkBottom(i + 1, j, tempOff3) + checkLeft(i, j - 1, tempOff3) + checkTop(i - 1, j, tempOff3))
        #officeList.append(checkLeft(i, j - 1, tempOff4) + checkTop(i - 1, j, tempOff4) + checkRight(i, j + 1, tempOff4))

        officeList.append(checkTop(i - 1, j, office) + checkRight(i, j + 1, office) + checkBottom(i + 1, j, office))
        officeList.append(checkRight(i, j + 1, office) + checkBottom(i + 1, j, office) + checkLeft(i, j - 1, office))
        officeList.append(checkBottom(i + 1, j, office) + checkLeft(i, j - 1, office) + checkTop(i - 1, j, office))
        officeList.append(checkLeft(i, j - 1, office) + checkTop(i - 1, j, office) + checkRight(i, j + 1, office))

        officeList.sort(key = lambda x:(-x[0]))

        ans += officeList[0][0]
        #office = [i[:] for i in officeList[0][1]]

    elif num == 3:
        officeList = []
        officeList.append(checkTop(i - 1, j, office) + checkRight(i, j + 1, office))
        officeList.append(checkRight(i, j + 1, office) + checkBottom(i + 1, j, office))
        officeList.append(checkBottom(i + 1, j, office) + checkLeft(i, j - 1, office))
        officeList.append(checkLeft(i, j - 1, office) + checkTop(i - 1, j, office))

        officeList.sort(key=lambda x: (-x[0]))
        ans += officeList[0][0]

    elif num == 2:
        officeList = []
        officeList.append(checkTop(i - 1, j, office) + checkBottom(i + 1, j, office))
        officeList.append(checkRight(i, j + 1, office) + checkLeft(i, j - 1, office))

        officeList.sort(key=lambda x: (-x[0]))
        ans += officeList[0][0]

    elif num == 1:
        officeList = []
        officeList.append(checkTop(i - 1, j, office))
        officeList.append(checkRight(i, j + 1, office))
        officeList.append(checkBottom(i + 1, j, office))
        officeList.append(checkLeft(i, j - 1, office))


        officeList.sort(key=lambda x: (-x[0]))
        ans += officeList[0][0]

    return ans

zero = 0
for i in range(N):
    office.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctvList.append([office[i][j], i, j])
        if office[i][j] == 0:
            zero += 1

cctvList.sort(key = lambda x : (-x[0]))
print(cctvList)

result = sol(office, cctvList)
print(zero - result)




