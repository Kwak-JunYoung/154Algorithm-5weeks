from collections import deque

def bfs():
    log[a] = 1
    queue = deque()
    queue.append(['', a])
    while queue:
        command, number = queue.popleft()
        D = number * 2 % 10000
        S = number - 1 if number >= 1 else 9999
        L = number % 1000 * 10 + number // 1000
        R = number // 10 + number % 10 * 1000

        if D == b:
            return command + 'D'
        elif log[D] == 0:
            log[D] = 1
            queue.append([command + 'D', D])

        if S == b:
            return command + 'S'
        elif log[S] == 0:
            log[S] = 1
            queue.append([command + 'S', S])

        if L == b:
            return command + 'L'
        elif log[L] == 0:
            log[L] = 1
            queue.append([command + 'L', L])

        if R == b:
            return command + 'R'
        elif log[R] == 0:
            log[R] = 1
            queue.append([command + 'R', R])

t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    log = [0 for _ in range(10000)]
    print(bfs())
