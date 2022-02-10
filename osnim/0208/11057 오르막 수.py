n = int(input())

dp = [0]*(n+2)

dp[1]=10
dp[2]=55
dp[3]=220

for i in range(4, n+1):
    dp[i] = 10*dp[i-1] - 330

print(dp[n])