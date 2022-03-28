import sys

N, M, K = map(int, sys.stdin.readline().split())

Team = 0

#girls = N//2

#boys = M//1

while True:
    if N + M <= K:
        print(Team)
        break

    N -= 2
    M -= 1
    Team += 1

    if N >= 0 and M >= 0:
        if N + M >= K:
            continue
        else:
            Team -= 1
            print(Team)
            break
    else:
        Team -= 1
        print(Team)
        break


