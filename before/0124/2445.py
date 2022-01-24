n = int(input())

for i in reversed(range(1, 2*n)):
    print('*' * (n-abs(n-i)) + " " * 2 * abs(i-n) + '*' * (n-abs(n-i)))