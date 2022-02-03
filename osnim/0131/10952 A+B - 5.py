from sys import stdin

while True:
    try:

        A, B = map(int, stdin.readline().split())
        # A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        print(A + B)

    except EOFError or ValueError:
        break
