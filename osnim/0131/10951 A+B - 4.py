from sys import stdin

while True:
    try:
        A, B = map(int, stdin.readline().split())
        #A, B = map(int, input().split())
        print(A+B)
    except EOFError or ValueError:
        break


import sys
for line in sys.stdin:
    A, B =map(int, line.split())
    print(A+B)