import sys
graph = []
N, L = map(int, sys.stdin.readline().split())
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def rowSol(L, result):
    for i in range(N):
        MIN = int(1e9)
        MAX = -1
        preNum = 0
        flag = 0  # 차이가 한번도 발생X
        continueFlag = False
        for j in range(N):
            # 행 검사
            num = graph[i][j]
            MIN = min(num, MIN)
            MAX = max(num, MAX)

            if abs(MIN - MAX) >= 2:
                continueFlag = True
                break
            if preNum != 0:  # 증가>감소 또는 감소>증가 경우 확인
                dif = num - preNum
                if flag == 0:
                    flag = dif
                elif flag * dif == -1:
                    continueFlag = True
                    break
            preNum = num

        if continueFlag:
            continue

        if MAX == MIN:  # 값이 계속 같은 경우
            result += 1
            print(i)
            continue

        minCnt = graph[i].count(MIN)

        if minCnt >= L:
            print(i)
            result += 1

    return result

def colSol(L, result):
    for i in range(N):
        MIN = int(1e9)
        MAX = -1
        preNum = 0
        flag = 0  # 차이가 한번도 발생X
        continueFlag = False
        for j in range(N):
            # 행 검사
            num = graph[j][i]
            MIN = min(num, MIN)
            MAX = max(num, MAX)
            if abs(MIN - MAX) >= 2:
                continueFlag = True
                break
            if preNum != 0:  # 증가>감소 또는 감소>증가 경우 확인
                dif = num - preNum
                if flag == 0:
                    flag = dif
                elif flag * dif == -1:
                    continueFlag = True
                    break
            preNum = num

        if continueFlag:
            continue

        if MAX == MIN:  # 값이 계속 같은 경우
            result += 1
            print(i)
            continue

        minCnt = 0
        for j in range(N):
            if graph[j][i] == MIN:
                minCnt += 1

        if minCnt >= L:
            print(i)
            result += 1

    return result

print(colSol(L, 0) + rowSol(L, 0))