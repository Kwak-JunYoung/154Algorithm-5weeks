n = int(input())

for i in reversed(range(1, 2*n)):
    print(" " * abs(i-n) + '*' * (n-abs(i-n)))