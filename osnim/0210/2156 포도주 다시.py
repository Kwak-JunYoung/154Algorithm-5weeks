n = int(input())

array = [0]*(n+1)

dp = [0]*(n+3)

for i in range(1, n+1):
    array[i] = int(input())

dp[1] = array[1]
#dp2[2] = array[1] + array[2]
#dp3[3] = array[2] + array[3]

MAX = 0

for i in range(1, n+1):

    dp[i] = max(dp[i-1], dp[i-2]+array[i], array[i-1]+ array[i] + dp[i-3])

print(dp[n])