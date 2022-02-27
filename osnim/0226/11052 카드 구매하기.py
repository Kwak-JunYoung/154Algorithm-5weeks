n = int(input())

a = list(map(int, input().split()))

print(a)

dp = [0]*(n+1)
#dp[0] = a[0]

for i in range(n):
    for j in range(0, i):
        dp[i] = max(dp[i-1]+a[0], a[i], a[j] )

print(dp)
print(dp[n-1])