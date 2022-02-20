n = int(input())
for i in range(n):
    if n == 1:
        print('*')
    else:
        if i == 0:
            print(' ' * (n - 1) + '*')
        elif i > 0 and i < n - 1:
            print(' '*(n - i - 1) + '*' + ' ' * (2*i - 1) + '*')
        else:
            print('*' * (i + n))
