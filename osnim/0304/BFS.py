from collections import deque

def BFS(graph, start, visited):
   queue = deque([start])
   visited[start] = True
   while queue:
      v = queue.popleft()
      print(v, end='')

      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True

graph = [
[],
[2, 6 ,8],
[1, 3, 5],
[2, 5],
[3, 5],
[2, 3, 4],
[1, 2, 7, 8],
[6],
[1, 6] ]

visited = [False]*(9)

BFS(graph, 1, visited)