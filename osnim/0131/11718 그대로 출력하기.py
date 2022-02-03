from sys import stdin

while True:
    try:
        line = input()
        print(line)
    except EOFError or ValueError:
        break


