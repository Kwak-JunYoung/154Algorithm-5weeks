import sys

R, C = map(int, sys.stdin.readline().split())
Graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
result = ''

# 행이 홀수일 경우
if R%2 == 1:
    for i in range(R):
        #홀수 번째 행
        if i % 2 == 0:
            result += 'R'*(C-1)
            if i == R-1:
                break
        #짝수 번째 행
        else:
            result += 'L'*(C-1)
        result += 'D'
    print(result)

#열이 홀수인 경우
elif C%2 == 1:
    for i in range(C):
        #홀수 번째 열
        if i % 2 == 0:
            result += 'D'*(R-1)
            if i == C-1:
                break
        #짝수 번째 열
        else:
            result += 'U'*(R-1)
        result += 'R'
    print(result)

#행, 열 모두 짝수인 경우 => x좌표,y좌표 인덱스 합이 홀수 중에서 가장 작은거 찾기

else:
    MIN = [1001, 0, 1] # 최소값, x좌표, y좌표
    PASS = False # 최소 지점을 지나간 경우를 표시
    
    for i in range(R):
        for j in range(C):
            if (i+j)%2 == 1:
                if MIN[0] > Graph[i][j]:
                    MIN = [Graph[i][j], i, j]
    #print(MIN)

    for i in range(0, R, 2):
        if PASS == False:
            # MIN의 행 인덱스가 i 또는 i+1 일 경우
            if MIN[1] == i:
                for j in range(1, C, 2):
                    # 행 인덱스가 짝수일 경우
                    if MIN[2] == j:
                        result += 'DR'
                        PASS = True
                    else:
                        if PASS == False:
                            result += 'DRUR'
                        else:
                            result += 'RURD'
                result += 'D'

            elif MIN[1] == i + 1:
                for j in range(0, C, 2):
                    # 행 인덱스가 홀수일 경우
                    if MIN[2] == j:
                        result += 'RD'
                        PASS = True
                    else:
                        if PASS == False:
                            result += 'DRUR'
                        else:
                            result += 'RURD'
                result += 'D'

            # 최솟값 안 지나고 MIN 행 인덱스가 i도 아니고 i+1 아닌 경우 ㄷ 반대 모양 만들기
            else:
                result += 'R' * (C-1) + 'D' + 'L' *(C-1) +'D'
        else:
            result += 'L' * (C - 1) + 'D' + 'R' * (C - 1) + 'D'

    print(result[0:-1])#마지막 D 는 뺌