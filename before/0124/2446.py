n = int(input())

for i in reversed(range(1, 2*n)):
    print(" " * ((n-1)-abs(i - n)) + '*' * (2 * abs(i-n) + 1))