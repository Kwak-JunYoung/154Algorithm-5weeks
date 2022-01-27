import sys

N = int(input())

for _ in range(N):
    result = []
    word = sys.stdin.readline().strip()
    for i in range(len(word)):
        if word[i] in "(":
            result.append(word[i])
        elif word[i] in ")":
            if len(result) <= 0:
                print("NO")
                break
            elif result[-1] in "(":
                result.pop(-1)
        if i == len(word)-1:
            if len(result) <= 0:
                print("YES")
            else:
                print("NO")