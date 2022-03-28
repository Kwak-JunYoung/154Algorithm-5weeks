import sys

R, C = map(int, sys.stdin.readline().split())
Graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
print(Graph)
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

#행, 열 모두 짝수인 경우 => 최소값 1개 찾아서 그 좌표는 이미 방문했다고 표시
else:
    # 왼쪽이 큰 경우
    if Graph[R-1][C-2] >= Graph[R-2][C-1]:
        for i in range(R-1):
            # 아래에서 2번째 행일때
            if i == R-2:
                result += 'DR' + 'URDR' * int((C-2)/2)

            # 홀수 번째 행
            elif i % 2 == 0:
                result += 'R' * (C - 1) + 'D'

            # 짝수 번째 행
            else:
                result += 'L' * (C - 1) + 'D'

    # 위쪽이 큰 경우
    else:
        for i in range(C-1):
            # 아래에서 2번째 행일때
            if i == C - 2:
                result += 'RD' + 'LDRD' * int((R - 2) / 2)

            # 홀수 번째 열
            elif i % 2 == 0:
                result += 'D' * (R - 1) + 'R'

            # 짝수 번째 열
            else:
                result += 'U' * (R - 1) + 'R'

print(result)