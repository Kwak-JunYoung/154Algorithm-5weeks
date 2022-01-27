import sys

N = int(input())
result = []
for _ in range(N):
    word = list(sys.stdin.readline().strip().split())
    if word[0] in "push":
        result.append(word[1])
    elif word[0] in "pop":
        if len(result) <= 0:
            print(-1)
        else:
            data = result.pop(-1)
            print(data)
    elif word[0] in "size":
        print(len(result))
    elif word[0] in "empty":
        if len(result) <= 0:
            print(1)
        else:
            print(0)
    elif word[0] in "top":
        if len(result) <= 0:
            print(-1)
        else:
            print(result[-1])