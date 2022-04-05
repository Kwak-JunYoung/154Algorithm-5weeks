import sys

N, M = map(int, sys.stdin.readline().split())
item_cost = list(map(int, sys.stdin.readline().split()))
#[list(map(int, sys.stdin.readline().split())) for _ in range(R)]
#items = [[-1]*3 for i in range(N+1)]
items = []
min_cost = item_cost

#dp = [-1]*(N+1)

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    #if a ==
    items.append([a, b, c])

items.sort(key = lambda x: x[0])

#for i in range(0, M):
#    dp[i] = min((item_list[i][1]+item_list[i][2]), min_cost)

def DFS(a):
    #print(visited)

    #min_cost = item_cost[v-1]
    if visited[a] == True:
        #print(min_cost[a-1])
        #print(a, min_cost)
        return min_cost[a-1]

    visited[a] = True

    for i in range(1, M):
        if items[i][0] == a:
            #print(min_cost[a-1])
            x = DFS(items[i][1])
            y = DFS(items[i][2])

            #print("x, y", x, y)

            min_cost[a-1] = min(item_cost[a-1], x + y)
            #print(items[i][1])
        #else:
            #min_cost[a - 1] = item_cost[a - 1]

    #print(a, min_cost)
    return min_cost[a - 1]

    '''
    if visited[v] == False:
        visited[v] = True
        min_cost[v] = min(item_cost[v-1], (DFS(items[v][1], visited) + DFS(items[v][2], visited)))
        return min_cost[v]
    '''

visited = [False] * (N+1)
visited[1] = True

#for i in range(M):
    #DFS(item_list, i, visited, min_cost)
    #print(min_cost)

#min_cost = DFS(items[1][1], visited) + DFS(items[1][2], visited)
#print(items)
#print(items[0][1])

print(DFS(items[0][1]) + DFS(items[0][2]))