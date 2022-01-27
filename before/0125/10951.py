while True:
    try:
        print(sum(list(map(int, input().split()))))
    except (EOFError):
        break