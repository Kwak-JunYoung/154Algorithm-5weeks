def dfs(graph, v, visited):
   visited[v] = True
   print(v, end='')

   for i in graph[v]:
      #print(i)
      if not visited[i]:
         dfs(graph, i, visited)

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

visited = [False]*9

dfs(graph, 1, visited)
