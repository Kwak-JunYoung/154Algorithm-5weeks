N, M, K = map(int, input().split())
team = 0

while N >= 2 and M >= 1 and M + N >= K + 3:
        N -= 2
        M -= 1
        team += 1

print(team)