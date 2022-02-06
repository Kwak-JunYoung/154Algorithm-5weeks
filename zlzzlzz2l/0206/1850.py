def gcd(a, b):
    if b == 0:
        return a

    A = a % b
    return gcd(b, A)

a, b = map(int, input().split())

n = gcd(a, b)
print('1' * n)