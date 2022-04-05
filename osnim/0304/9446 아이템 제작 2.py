import sys

N, M = map(int, sys.stdin.readline().split())
min_cost = [0]+list(map(int, sys.stdin.readline().split()))
items = [[] for i in range(N+1)]
#items = []

#dp = [-1]*(N+1)

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    items[a].append([b, c])

print(items)

if not items[0]:
    print("empty")
else:
    print("11")

def DFS(a):
    visited[a] = True

    if not items[a]:
        return min_cost[a]

    for i in items[a]:

        temp = 0
        if visited[i] == False:
            min_cost[a] += DFS(i)
    return min_cost[a]

visited = [False] * (N+1)

DFS(1)
#print(DFS(1))
