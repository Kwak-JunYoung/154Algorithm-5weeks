a, b = map(int, input().split())


def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)


gcd = gcd(a, b)
lcm = int((a * b) / gcd)
print(f'{gcd}\n{lcm}')
