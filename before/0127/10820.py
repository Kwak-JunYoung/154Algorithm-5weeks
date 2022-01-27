while True:
    try:
        s = input()
        length = len(s)
        low = 0
        up = 0
        n = 0
        space = 0
        for i in range(length):
            if s[i].isupper():
                up += 1
            elif s[i].islower():
                low += 1
            elif s[i].isdigit():
                n += 1
            elif s[i] == ' ':
                space += 1
        print(low, up, n, space)

    except (EOFError):
        break