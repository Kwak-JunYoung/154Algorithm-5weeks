import sys
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    word = list(sys.stdin.readline().strip().split())
    if word[0] == 'push_front':
        q.appendleft(word[1])
    elif word[0] == 'push_back':
        q.append(word[1])
    elif word[0] == 'pop_front':
        if len(q) <= 0:
            print(-1)
        else:
            data = q.popleft()
            print(data)
    elif word[0] == 'pop_back':
        if len(q) <= 0:
            print(-1)
        else:
            data = q.pop()
            print(data)
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        if len(q) <= 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(q) <= 0:
            print(-1)
        else:
            print(q[0])
    elif word[0] == 'back':
        if len(q) <= 0:
            print(-1)
        else:
            print(q[-1])