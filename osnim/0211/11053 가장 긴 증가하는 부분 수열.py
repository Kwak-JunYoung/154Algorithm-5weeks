n = int(input())

array = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))