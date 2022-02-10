n = int(input())

# dp = [0] * (n+1) 인덱스에러
dp = [0] * (n+2)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)