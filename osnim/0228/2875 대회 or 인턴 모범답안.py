import sys

N, M, K = map(int, sys.stdin.readline().split())

Team = 0

# 여자 2명, 남자 1명 팀을 만들고 인턴쉽도 보낼 수 있을 때
while N >= 2 and M >= 1 and N + M >= K + 3:
    N -= 2
    M -= 1
    Team += 1

print(Team)


'''

while True:
    N -= 2
    M -= 1

    if N < 0 or M < 0 or (N + M) < K:
        break
    Team += 1

print(Team)
'''
