import sys

H, S = map(int, sys.stdin.readline().split())
cook = int(sys.stdin.readline().rstrip())

S = S + cook

H += S//60
S =  S%60

if H >= 24:
    H %= 24

print(H, S)