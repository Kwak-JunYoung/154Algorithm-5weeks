import sys
from collections import deque

N = int(input())
p = deque()
for _ in range(N):
    word = list(sys.stdin.readline().strip().split())
    if word[0] in 'push':
        p.append(word[1])
    elif word[0] in 'pop':
        if len(p) <= 0:
            print(-1)
        else:
            data = p.popleft()
            print(data)
    elif word[0] in 'size':
        print(len(p))
    elif word[0] in 'empty':
        if len(p) > 0:
            print(0)
        else:
            print(1)
    elif word[0] in 'front':
        if len(p) <= 0:
            print(-1)
        else:
            print(p[0])
    elif word[0] in 'back':
        if len(p) <= 0:
            print(-1)
        else:
            print(p[-1])