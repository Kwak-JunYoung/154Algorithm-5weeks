n = int(input())
for i in range(n):
    if n == 1:
        print('*')
    else:
        print(' '*(n - i - 1) + '* ' * i + '*')
