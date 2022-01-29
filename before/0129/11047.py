n, k = list(map(int, input().split()))

prices = sorted([int(input()) for _ in range(n)])

count = 0
for price in reversed(prices):
    if k // price > 0:
        count += k // price
        k %= price

print(count)