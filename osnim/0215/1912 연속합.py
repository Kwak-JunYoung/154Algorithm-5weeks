#시간초과

n = int(input())

a = list(map(int, input().split()))

dp = [0]*(n)

SUM = 0

for i in range(n):
    SUM = 0
    dp[i] = a[i]
    for j in range(i+1):
        SUM = 0
        for k in range(j, i+1):
            #dp[i] = max(SUM, dp[i])
            SUM += a[k]

        #print(SUM)
        dp[i] = max(SUM, dp[i])

    #print(dp)
print(max(dp))