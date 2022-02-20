n = int(input())
k = n
n = 2 * n
for i in range(1, n):
    if i <= n / 2:
        print('*' * i + ' ' * (n - (i*2)) + '*' * i)
    elif i == n / 2:
        print('*' * (i * 2))
    else:
        print('*' * (n-i) + ' ' * ((i - k)+1) + '*' * (n-i))
        k = k - 1
