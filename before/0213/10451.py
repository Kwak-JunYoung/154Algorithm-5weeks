t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    # print(arr)
    visited = [False] * (n + 1)
    visited[0] = True
    ans = 0
    while False in visited:
        i = visited.index(False)
        stack = [i]
        while stack:
            cur = stack.pop()
            visited[cur] = True
            if visited[arr[cur]] == False:
                stack.append(arr[cur])
        ans += 1
    print(ans)
    