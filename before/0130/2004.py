n, m = list(map(int, input().split()))

def counts(x, n):
    cnts = 0
    while x:
        x //= n
        cnts += x
    return cnts

two_a = counts(n, 2)
two_b = counts(m, 2)
two_c = counts(n - m, 2)

x = two_a - two_b - two_c

five_a = counts(n, 5)
five_b = counts(m, 5)
five_c = counts(n - m, 5)

y = five_a - five_b - five_c

print(min(x, y))