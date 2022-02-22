import sys
from collections import deque

def dfs( m,v):
    arr_visited_dfs[v] = True
    print(v, end=" ")
    for i in range(2*m):
        if arr_node[i][0] == v and arr_visited_dfs[arr_node[i][1]]== False:
            dfs(m, arr_node[i][1])

def bfs(m, v):
    queue.append(v)
    arr_visited_bfs[v] = True
    while queue:   
        v = queue.popleft()
        for i in range(2*m):
            if arr_node[i][0] == v and arr_visited_bfs[arr_node[i][1]] == False:
                queue.append(arr_node[i][1])
                arr_visited_bfs[arr_node[i][1]] = True
        print(v, end=" ")
        

n , m , v = map(int, input().split())

arr_node = []
arr_visited_dfs = [False] * (n+1)
arr_visited_bfs = [False] * (n+1)
queue = deque()

# 노드 번호 저장할 2차원 배열 생성
for i in range(2*m):
    arr_node.append([])
    for j in range(2):
        arr_node[i].append(0)

# 배열에 노드 번호 저장
for i in range(m):
    v1, v2 = sys.stdin.readline().strip().split()
    arr_node[i][0] = int(v1)
    arr_node[i][1] = int(v2)

    # 양방향
    arr_node[2*m-1-i][0] = int(v2)
    arr_node[2*m-1-i][1] = int(v1)

arr_node = sorted(arr_node)

# # 출력
# print('arr_node')
# for i in range(2*m):
#     for j in range(2):
#         print(arr_node[i][j], end=' ')
#     print()
# print('\n\n')

dfs(m, v)
print()
bfs(m, v)


'''
1. 양방향으로 노드번호 저장해야함
2. 주어지는 (두 정점의 번호)가 3 4 / 3 1 로 나오는 경우 3 다음에    4가 시작됨
    --> 정렬을 해준다.
3. bfs 에서 v = queue.popleft()를 for문 전에 해야함
이유 : for문 뒤로 해버리면 만약 v=3이라면 3 1 이 돌고 popleft가 되버려서 v=3인 상황이 한번더 반복되어 3 4까지도 실행이 되버림
4. arr_node 배열 저장할때, int 형식으로 저장해야함! (안하면 문자열 형식으로 들어감)
'''

''' 다른 사람 코드
배열에 값 저장할 때
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

'''