n = int(input())

for i in range(n):
    line = ''
    if i == (n-1):
        line = '*' * (2 * n - 1)
    else:
        line = ' ' * (n-i-1) + '*' + ' ' * (2 * i - 1)
        if i != 0:
            line += '*'
    print(line)
