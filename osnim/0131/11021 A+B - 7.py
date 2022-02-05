from sys import stdin

T = int(stdin.readline().rstrip())
# T = int(input())
for i in range(1, T + 1):
    A, B = map(int, stdin.readline().split())
    print("Case #" + str(i) + ":", A + B)
