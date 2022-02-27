n = int(input())

dp = [0]*(n+2)

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):

    if i%2 == 0:
        dp[i] = dp[i-2] * 3 + 2

    else:
        dp[i] = dp[i-1]

print(dp[n])