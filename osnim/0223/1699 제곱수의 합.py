#kadane's 알고리즘 O(N)

n = int(input())

a = list(map(int, input().split()))

dp = [-10001]*(n+1)

for i in range(n):

    dp[i] = max(dp[i-1]+a[i], a[i])

print(max(dp))