n = int(input())
for i in range(n):
    row = ''
    for j in range(2*i + 1):
        if j % 2 == 0:
            row += '* '
    print(' ' * (n - i - 1) + row)