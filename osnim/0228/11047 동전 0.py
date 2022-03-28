import sys

N, K = map(int, sys.stdin.readline().split())

coin_list = []

for i in range(N):
    coin_list.append(int(sys.stdin.readline()))

result = 0

for i in range(N):
    coin = coin_list.pop()

    if K <= 0:
        break

    if K // coin >= 0:
        result += K // coin
        K = K - coin * (K // coin)
        if K <= 0:
            break

print(result)
